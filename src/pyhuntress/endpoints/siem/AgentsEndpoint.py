from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.siem.AgentsIdEndpoint import AgentsIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.siem import SIEMAgents
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSIEMRequestParams,
)


class AgentsEndpoint(
    HuntressEndpoint,
    IGettable[SIEMAgents, HuntressSIEMRequestParams],
    IPaginateable[SIEMAgents, HuntressSIEMRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "agents", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SIEMAgents)
        IPaginateable.__init__(self, SIEMAgents)

    def id(self, id: int) -> AgentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized AgentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            AgentsIdEndpoint: The initialized AgentsIdEndpoint object.
        """
        child = AgentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSIEMRequestParams | None = None,
    ) -> PaginatedResponse[SIEMAgents]:
        """
        Performs a GET request against the /agents endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SIEMAgents]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["limit"] = limit
        else:
            params = {"page": page, "limit": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SIEMAgents,
            self,
            "agents",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSIEMRequestParams | None = None,
    ) -> SIEMAgents:
        """
        Performs a GET request against the /agents endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SIEMAuthInformation: The parsed response data.
        """
        return self._parse_many(
            SIEMAgents,
            super()._make_request("GET", data=data, params=params).json().get('agents', {}),
        )
