from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
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


class AccountsIdPhishingCampaignsEndpoint(
    HuntressEndpoint,
    IGettable[SATPhishingCampaigns, HuntressSATRequestParams],
    IPaginateable[SATPhishingCampaigns, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "phishing-campaigns", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATPhishingCampaigns)
        IPaginateable.__init__(self, SATPhishingCampaigns)

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATPhishingCampaigns]:
        """
        Performs a GET request against the /accounts/{id}/phishing-campaigns endpoint and returns an initialized PaginatedResponse object.

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
        Performs a GET request against the /accounts/{id}/phishing-campaigns endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATPhishingCampaigns: The parsed response data.
        """
        return self._parse_many(
            SATPhishingCampaigns,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
