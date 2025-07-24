from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.LearnersIdEndpoint import LearnersIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATLearners
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class LearnersEndpoint(
    HuntressEndpoint,
    IGettable[SATLearners, HuntressSATRequestParams],
    IPaginateable[SATLearners, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "learners", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATLearners)
        IPaginateable.__init__(self, SATLearners)

    def id(self, id: int) -> LearnersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized LearnersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            LearnersIdEndpoint: The initialized LearnersIdEndpoint object.
        """
        child = LearnersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATLearners]:
        """
        Performs a GET request against the /learners endpoitments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATLearners]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SATLearners,
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
    ) -> SATLearners:
        """
        Performs a GET request against the /learners endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATLearners: The parsed response data.
        """
        return self._parse_many(
            SATLearners,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
