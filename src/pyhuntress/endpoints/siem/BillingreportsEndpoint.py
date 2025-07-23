from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.siem import SIEMBillingReports
from pyhuntress.types import (
    JSON,
    HuntressSIEMRequestParams,
)


class BillingreportsEndpoint(
    HuntressEndpoint,
    IGettable[SIEMBillingReports, HuntressSIEMRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "billing_reports", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SIEMBillingReports)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSIEMRequestParams | None = None,
    ) -> SIEMBillingReports:
        """
        Performs a GET request against the /Billing_reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SIEMAuthInformation: The parsed response data.
        """
        return self._parse_many(
            SIEMBillingReports,
            super()._make_request("GET", data=data, params=params).json().get('billing_reports', {}),
        )
