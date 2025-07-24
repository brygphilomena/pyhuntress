from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.AssignmentsIdEndpoint import AssignmentsIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATAssignments
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class AssignmentsEndpoint(
    HuntressEndpoint,
    IGettable[SATAssignments, HuntressSATRequestParams],
    IPaginateable[SATAssignments, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "assignments", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATAssignments)
        IPaginateable.__init__(self, SATAssignments)

    def id(self, id: int) -> AssignmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized AssignmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            AssignmentsIdEndpoint: The initialized AssignmentsIdEndpoint object.
        """
        child = AssignmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATAssignments]:
        """
        Performs a GET request against the /assignments endpoint and returns an initialized PaginatedResponse object.

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
            SATAssignments,
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
    ) -> SATAssignments:
        """
        Performs a GET request against the /assignments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATAssignments: The parsed response data.
        """
        return self._parse_many(
            SATAssignments,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
