from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.siem import SIEMAccount
from pyhuntress.types import (
    JSON,
    HuntressSIEMRequestParams,
)


class AccountEndpoint(
    HuntressEndpoint,
    IGettable[SIEMAccount, HuntressSIEMRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "account", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SIEMAccount)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSIEMRequestParams | None = None,
    ) -> SIEMAccount:
        """
        Performs a GET request against the /account endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SIEMAuthInformation: The parsed response data.
        """
        return self._parse_one(
            SIEMAccount,
            super()._make_request("GET", data=data, params=params).json().get('account', {}),
        )
