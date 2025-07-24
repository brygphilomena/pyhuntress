from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.PhishingCampaignScenariosIdAttemptsEndpoint import PhishingCampaignScenariosIdAttemptsEndpoint
from pyhuntress.endpoints.managedsat.PhishingCampaignScenariosIdCampaignEndpoint import PhishingCampaignScenariosIdCampaignEndpoint
from pyhuntress.endpoints.managedsat.PhishingCampaignScenariosIdScenarioEndpoint import PhishingCampaignScenariosIdScenarioEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATPhishingScenarios
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class PhishingCampaignScenariosIdEndpoint(
    HuntressEndpoint,
    IGettable[SATPhishingScenarios, HuntressSATRequestParams],
    IPaginateable[SATPhishingScenarios, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATPhishingScenarios)
        IPaginateable.__init__(self, SATPhishingScenarios)

        self.attempts = self._register_child_endpoint(PhishingCampaignScenariosIdAttemptsEndpoint(client, parent_endpoint=self))
        self.campaign = self._register_child_endpoint(PhishingCampaignScenariosIdCampaignEndpoint(client, parent_endpoint=self))
        self.campaign = self._register_child_endpoint(PhishingCampaignScenariosIdScenarioEndpoint(client, parent_endpoint=self))

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATPhishingScenarios]:
        """
        Performs a GET request against the /phishing-campaigns/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATPhishingScenarios]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SATPhishingScenarios,
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
    ) -> SATPhishingScenarios:
        """
        Performs a GET request against the /phishing-campaigns/{id} endpoint.

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
