from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.PhishingCampaignScenariosIdEndpoint import PhishingCampaignScenariosIdEndpoint
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


class PhishingCampaignScenariosEndpoint(
    HuntressEndpoint,
    IGettable[SATPhishingScenarios, HuntressSATRequestParams],
    IPaginateable[SATPhishingScenarios, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "phishing-campaign-scenarios", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATPhishingScenarios)
        IPaginateable.__init__(self, SATPhishingScenarios)

    def id(self, id: int) -> PhishingCampaignScenariosIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized PhishingCampaignScenariosIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            PhishingCampaignScenariosIdEndpoint: The initialized PhishingCampaignScenariosIdEndpoint object.
        """
        child = PhishingCampaignScenariosIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATPhishingScenarios]:
        """
        Performs a GET request against the /phishing-campaign-scenarios endpoints endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATData]: The initialized PaginatedResponse object.
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
        Performs a GET request against the /phishing-campaign-scenarios endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATPhishingScenarios: The parsed response data.
        """
        return self._parse_many(
            SATPhishingScenarios,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
