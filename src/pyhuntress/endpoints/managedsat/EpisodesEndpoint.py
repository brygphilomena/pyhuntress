from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.EpisodesIdEndpoint import EpisodesIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATEpisodes
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class EpisodesEndpoint(
    HuntressEndpoint,
    IGettable[SATEpisodes, HuntressSATRequestParams],
    IPaginateable[SATEpisodes, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "episodes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATEpisodes)
        IPaginateable.__init__(self, SATEpisodes)

    def id(self, id: int) -> EpisodesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized EpisodesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            EpisodesIdEndpoint: The initialized EpisodesIdEndpoint object.
        """
        child = EpisodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATEpisodes]:
        """
        Performs a GET request against the /episodes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATData]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SATEpisodes,
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
    ) -> SATEpisodes:
        """
        Performs a GET request against the /episodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATEpisodes: The parsed response data.
        """
        return self._parse_many(
            SATEpisodes,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
