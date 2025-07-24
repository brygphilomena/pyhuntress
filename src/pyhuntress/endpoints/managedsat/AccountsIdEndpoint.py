from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.AccountsIdUsersEndpoint import AccountsIdUsersEndpoint
from pyhuntress.endpoints.managedsat.AccountsIdAssignmentsEndpoint import AccountsIdAssignmentsEndpoint
from pyhuntress.endpoints.managedsat.AccountsIdDepartmentsEndpoint import AccountsIdDepartmentsEndpoint
from pyhuntress.endpoints.managedsat.AccountsIdGroupsEndpoint import AccountsIdGroupsEndpoint
from pyhuntress.endpoints.managedsat.AccountsIdLearnersEndpoint import AccountsIdLearnersEndpoint
from pyhuntress.endpoints.managedsat.AccountsIdPhishingCampaignsEndpoint import AccountsIdPhishingCampaignsEndpoint
from pyhuntress.endpoints.managedsat.AccountsIdPhishingScenariosEndpoint import AccountsIdPhishingScenariosEndpoint
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


class AccountsIdEndpoint(
    HuntressEndpoint,
    IGettable[SATAccounts, HuntressSATRequestParams],
    IPaginateable[SATAccounts, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATAccounts)
        IPaginateable.__init__(self, SATAccounts)

        self.users = self._register_child_endpoint(AccountsIdUsersEndpoint(client, parent_endpoint=self))
        self.assignments = self._register_child_endpoint(AccountsIdAssignmentsEndpoint(client, parent_endpoint=self))
        self.departments = self._register_child_endpoint(AccountsIdDepartmentsEndpoint(client, parent_endpoint=self))
        self.groups = self._register_child_endpoint(AccountsIdGroupsEndpoint(client, parent_endpoint=self))
        self.learners = self._register_child_endpoint(AccountsIdLearnersEndpoint(client, parent_endpoint=self))
        self.phishing_campaigns = self._register_child_endpoint(AccountsIdPhishingCampaignsEndpoint(client, parent_endpoint=self))
        self.phishing_scenarios = self._register_child_endpoint(AccountsIdPhishingScenariosEndpoint(client, parent_endpoint=self))

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSATRequestParams | None = None,
    ) -> SATAccounts:
        """
        Performs a GET request against the /accounts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATAccountsInformation: The parsed response data.
        """
        return self._parse_one(
            SATAccounts,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
