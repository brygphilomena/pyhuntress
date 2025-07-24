from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.PhishingAttemptsActionsReportEndpoint import PhishingAttemptsActionsReportEndpoint
from pyhuntress.interfaces import (
    IPostable,
)
from pyhuntress.models.managedsat import SATPhishingAttemptsReport
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class PhishingAttemptsActionsEndpoint(
    HuntressEndpoint,
    IPostable[SATPhishingAttemptsReport, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "actions", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, SATPhishingAttemptsReport)

        self.report = self._register_child_endpoint(PhishingAttemptsActionsReportEndpoint(client, parent_endpoint=self))
