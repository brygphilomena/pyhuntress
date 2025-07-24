from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.managedsat import SATPhishingScenarios
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class PhishingCampaignScenariosIdScenarioEndpoint(
    HuntressEndpoint,
    IGettable[SATPhishingScenarios, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "scenario", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATPhishingScenarios)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSATRequestParams | None = None,
    ) -> SATPhishingScenarios:
        
        """
        Performs a GET request against the /phishing-campaign-scenarios/{id}/scenario endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATPhishingScenarios: The parsed response data.
        """
        return self._parse_one(
            SATPhishingScenarios,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
