from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.PhishingAttemptsActionsEndpoint import PhishingAttemptsActionsEndpoint
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
        HuntressEndpoint.__init__(self, client, "phishing-attempts", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, SATPhishingAttemptsReport)

        self.actions = self._register_child_endpoint(PhishingAttemptsActionsEndpoint(client, parent_endpoint=self))
