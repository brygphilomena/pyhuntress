from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.siem.SignalsIdEndpoint import SignalsIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.siem import SIEMSignals
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSIEMRequestParams,
)


class SignalsEndpoint(
    HuntressEndpoint,
    IGettable[SIEMSignals, HuntressSIEMRequestParams],
    IPaginateable[SIEMSignals, HuntressSIEMRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "signals", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SIEMSignals)
        IPaginateable.__init__(self, SIEMSignals)

    def id(self, id: int) -> SignalsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SignalsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SignalsIdEndpoint: The initialized SignalsIdEndpoint object.
        """
        child = SignalsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSIEMRequestParams | None = None,
    ) -> PaginatedResponse[SIEMSignals]:
        """
        Performs a GET request against the /signals endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SIEMSignals]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["limit"] = limit
        else:
            params = {"page": page, "limit": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SIEMSignals,
            self,
            "signals",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSIEMRequestParams | None = None,
    ) -> SIEMSignals:
        """
        Performs a GET request against the /signals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SIEMAuthInformation: The parsed response data.
        """
        return self._parse_many(
            SIEMSignals,
            super()._make_request("GET", data=data, params=params).json().get('signals', {}),
        )
