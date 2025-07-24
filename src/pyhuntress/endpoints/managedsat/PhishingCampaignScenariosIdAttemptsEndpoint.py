from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.managedsat import SATPhishingCampaignAttempts
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class PhishingCampaignScenariosIdAttemptsEndpoint(
    HuntressEndpoint,
    IGettable[SATPhishingCampaignAttempts, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "attempts", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATPhishingCampaignAttempts)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSATRequestParams | None = None,
    ) -> SATPhishingCampaignAttempts:
        
        """
        Performs a GET request against the /accounts/{id}/attempts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATPhishingCampaignAttempts: The parsed response data.
        """
        return self._parse_many(
            SATPhishingCampaignAttempts,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
