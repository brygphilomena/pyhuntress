from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.DepartmentsIdEndpoint import DepartmentsIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATDepartments
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class DepartmentsEndpoint(
    HuntressEndpoint,
    IGettable[SATDepartments, HuntressSATRequestParams],
    IPaginateable[SATDepartments, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "departments", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATDepartments)
        IPaginateable.__init__(self, SATDepartments)

    def id(self, id: int) -> DepartmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized DepartmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            DepartmentsIdEndpoint: The initialized DepartmentsIdEndpoint object.
        """
        child = DepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATDepartments]:
        """
        Performs a GET request against the /departments endpoitments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATDepartments]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SATDepartments,
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
    ) -> SATDepartments:
        """
        Performs a GET request against the /departments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATDepartments: The parsed response data.
        """
        return self._parse_many(
            SATDepartments,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
