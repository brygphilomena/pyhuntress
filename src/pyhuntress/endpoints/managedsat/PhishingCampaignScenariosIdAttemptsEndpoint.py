from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATPhishingCampaignAttempts
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class PhishingCampaignScenariosIdAttemptsEndpoint(
    HuntressEndpoint,
    IGettable[SATPhishingCampaignAttempts, HuntressSATRequestParams],
    IPaginateable[SATPhishingCampaignAttempts, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "attempts", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATPhishingCampaignAttempts)
        IPaginateable.__init__(self, SATPhishingCampaignAttempts)

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATPhishingCampaignAttempts]:
        """
        Performs a GET request against the /phishing-campaign-scenarios/{id}/attempts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATPhishingCampaignAttempts]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SATPhishingCampaignAttempts,
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
