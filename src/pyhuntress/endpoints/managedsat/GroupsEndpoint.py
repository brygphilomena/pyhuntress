from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.GroupsIdEndpoint import GroupsIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATGroups
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class GroupsEndpoint(
    HuntressEndpoint,
    IGettable[SATGroups, HuntressSATRequestParams],
    IPaginateable[SATGroups, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "groups", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATGroups)
        IPaginateable.__init__(self, SATGroups)

    def id(self, id: int) -> GroupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized GroupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            GroupsIdEndpoint: The initialized GroupsIdEndpoint object.
        """
        child = GroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATGroups]:
        """
        Performs a GET request against the /groups endpoitments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATGroups]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SATGroups,
            self,
            "data",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSATRequestParams | None = None,
    ) -> SATGroups:
        """
        Performs a GET request against the /groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATGroups: The parsed response data.
        """
        return self._parse_many(
            SATGroups,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
