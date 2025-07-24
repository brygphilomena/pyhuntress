from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.AccountsIdEndpoint import AccountsIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATAccounts
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class AccountsEndpoint(
    HuntressEndpoint,
    IGettable[SATAccounts, HuntressSATRequestParams],
    IPaginateable[SATAccounts, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "accounts", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATAccounts)
        IPaginateable.__init__(self, SATAccounts)

    def id(self, id: int) -> AccountsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized AccountsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            AccountsIdEndpoint: The initialized AccountsIdEndpoint object.
        """
        child = AccountsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATAccounts]:
        """
        Performs a GET request against the /accounts endpoint and returns an initialized PaginatedResponse object.

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
            SATAccounts,
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
    ) -> SATAccounts:
        """
        Performs a GET request against the /accounts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATAccountInformation: The parsed response data.
        """
        return self._parse_many(
            SATAccounts,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
