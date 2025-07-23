from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
    from pydantic import BaseModel
    from requests import Response

    from pyhuntress.clients.huntress_client import HuntressClient
    from pyhuntress.types import (
        RequestData,
        RequestMethod,
        RequestParams,
    )

TChildEndpoint = TypeVar("TChildEndpoint", bound="HuntressEndpoint")
TModel = TypeVar("TModel", bound="BaseModel")


class HuntressEndpoint:
    """
    HuntressEndpoint is a base class for all Huntress API endpoint classes.
    It provides a generic implementation for interacting with the Huntress API,
    handling requests, parsing responses into model instances, and managing pagination.

    HuntressEndpoint makes use of a generic type variable TModel, which represents
    the expected HuntressModel type for the endpoint. This allows for type-safe
    handling of model instances throughout the class.

    Each derived class should specify the HuntressModel type it will be working with
    when inheriting from HuntressEndpoint. For example:
    class CompanyEndpoint(HuntressEndpoint[CompanyModel]).

    HuntressEndpoint provides methods for making API requests and handles pagination
    using the PaginatedResponse class. By default, most CRUD methods raise a
    NotImplementedError, which should be overridden in derived classes to provide
    endpoint-specific implementations.

    HuntressEndpoint also supports handling nested endpoints, which are referred to as
    child endpoints. Child endpoints can be registered and accessed through their parent
    endpoint, allowing for easy navigation through related resources in the API.

    Args:
        client: The HuntressAPIClient instance.
        endpoint_url (str): The base URL for the specific endpoint.
        parent_endpoint (HuntressEndpoint, optional): The parent endpoint, if applicable.

    Attributes:
        client (HuntressAPIClient): The HuntressAPIClient instance.
        endpoint_url (str): The base URL for the specific endpoint.
        _parent_endpoint (HuntressEndpoint): The parent endpoint, if applicable.
        model_parser (ModelParser): An instance of the ModelParser class used for parsing API responses.
        _model (Type[TModel]): The model class for the endpoint.
        _id (int): The ID of the current resource, if applicable.
        _child_endpoints (List[HuntressEndpoint]): A list of registered child endpoints.

    Generic Type:
        TModel: The model class for the endpoint.
    """

    def __init__(
        self,
        client: HuntressClient,
        endpoint_url: str,
        parent_endpoint: HuntressEndpoint | None = None,
    ) -> None:
        """
        Initialize a HuntressEndpoint instance with the client and endpoint base.

        Args:
            client: The HuntressAPIClient instance.
            endpoint_base (str): The base URL for the specific endpoint.
        """
        self.client = client
        self.endpoint_base = endpoint_url
        self._parent_endpoint = parent_endpoint
        self._id = None
        self._child_endpoints: list[HuntressEndpoint] = []

    def _register_child_endpoint(self, child_endpoint: TChildEndpoint) -> TChildEndpoint:
        """
        Register a child endpoint to the current endpoint.

        Args:
            child_endpoint (HuntressEndpoint): The child endpoint instance.

        Returns:
            HuntressEndpoint: The registered child endpoint.
        """
        self._child_endpoints.append(child_endpoint)
        return child_endpoint

    def _url_join(self, *args) -> str:  # noqa: ANN002
        """
        Join URL parts into a single URL string.

        Args:
            *args: The URL parts to join.

        Returns:
            str: The joined URL string.
        """
        url_parts = [str(arg).strip("/") for arg in args]
        return "/".join(url_parts)

    def _get_replaced_url(self) -> str:
        if self._id is None:
            return self.endpoint_base
        return self.endpoint_base.replace("{id}", str(self._id))

    def _make_request(
        self,
        method: RequestMethod,
        endpoint: HuntressEndpoint | None = None,
        data: RequestData | None = None,
        params: RequestParams | None = None,
        headers: dict[str, str] | None = None,
        stream: bool = False,  # noqa: FBT001, FBT002
    ) -> Response:
        """
        Make an API request using the specified method, endpoint, data, and parameters.
        This function isn't intended for use outside of this class.
        Please use the available CRUD methods as intended.

        Args:
            method (str): The HTTP method to use for the request (e.g., GET, POST, PUT, etc.).
            endpoint (str, optional): The endpoint to make the request to.
            data (dict, optional): The request data to send.
            params (dict, optional): The query parameters to include in the request.

        Returns:
            The Response object (see requests.Response).

        Raises:
            Exception: If the request returns a status code >= 400.
        """
        url = self._get_endpoint_url()
        if endpoint:
            url = self._url_join(url, endpoint)

        return self.client._make_request(method, url, data, params, headers, stream)

    def _build_url(self, other_endpoint: HuntressEndpoint) -> str:
        if other_endpoint._parent_endpoint is not None:
            parent_url = self._build_url(other_endpoint._parent_endpoint)
            if other_endpoint._parent_endpoint._id is not None:
                return self._url_join(
                    parent_url,
                    other_endpoint._get_replaced_url(),
                )
            else:  # noqa: RET505
                return self._url_join(parent_url, other_endpoint._get_replaced_url())
        else:
            return self._url_join(self.client._get_url(), other_endpoint._get_replaced_url())

    def _get_endpoint_url(self) -> str:
        return self._build_url(self)

    def _parse_many(self, model_type: type[TModel], data: list[dict[str, Any]]) -> list[TModel]:
        return [model_type.model_validate(d) for d in data]

    def _parse_one(self, model_type: type[TModel], data: dict[str, Any]) -> TModel:
        return model_type.model_validate(data)
