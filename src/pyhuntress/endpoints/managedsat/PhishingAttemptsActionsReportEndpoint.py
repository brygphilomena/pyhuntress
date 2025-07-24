from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IPostable,
)
from pyhuntress.models.managedsat import SATPhishingAttemptsReport
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class PhishingAttemptsActionsReportEndpoint(
    HuntressEndpoint,
    IPostable[SATPhishingAttemptsReport, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "report", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, SATPhishingAttemptsReport)

#    def post(self, data: JSON | None = None, params: HuntressSATRequestParams | None = None) -> SATUsers:
#        """
#        Performs a POST request against the /company/companies endpoint.
#
#        Parameters:
#            data (dict[str, Any]): The data to send in the request body.
#            params (dict[str, int | str]): The parameters to send in the request query string.
#        Returns:
#            SATUsers: The parsed response data.
#        """
#        return self._parse_one(SATUsers, super()._make_request("POST", data=data, params=params).json())
