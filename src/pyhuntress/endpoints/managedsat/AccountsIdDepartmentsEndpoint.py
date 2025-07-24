from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.managedsat import SATDepartments
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class AccountsIdDepartmentsEndpoint(
    HuntressEndpoint,
    IGettable[SATDepartments, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "departments", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATDepartments)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSATRequestParams | None = None,
    ) -> SATDepartments:
        
        """
        Performs a GET request against the /accounts/{id}/departments endpoint.

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
