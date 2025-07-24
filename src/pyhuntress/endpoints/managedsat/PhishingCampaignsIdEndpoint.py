from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.PhishingCampaignsIdAttemptsEndpoint import PhishingCampaignsIdAttemptsEndpoint
from pyhuntress.endpoints.managedsat.PhishingCampaignsIdCampaignScenariosEndpoint import PhishingCampaignsIdCampaignScenariosEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATPhishingCampaigns
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class PhishingCampaignsIdEndpoint(
    HuntressEndpoint,
    IGettable[SATPhishingCampaigns, HuntressSATRequestParams],
    IPaginateable[SATPhishingCampaigns, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATPhishingCampaigns)
        IPaginateable.__init__(self, SATPhishingCampaigns)

        self.attempts = self._register_child_endpoint(PhishingCampaignsIdAttemptsEndpoint(client, parent_endpoint=self))
        self.campaign_scenarios = self._register_child_endpoint(PhishingCampaignsIdCampaignScenariosEndpoint(client, parent_endpoint=self))

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATPhishingCampaigns]:
        """
        Performs a GET request against the /phishing-campaigns/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATPhishingCampaigns]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SATPhishingCampaigns,
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
    ) -> SATPhishingCampaigns:
        """
        Performs a GET request against the /phishing-campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATPhishingCampaigns: The parsed response data.
        """
        return self._parse_one(
            SATPhishingCampaigns,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
