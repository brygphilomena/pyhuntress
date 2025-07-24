from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.siem.BillingreportsIdEndpoint import BillingIdreportsEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.siem import SIEMBillingReports
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSIEMRequestParams,
)


class BillingreportsEndpoint(
    HuntressEndpoint,
    IGettable[SIEMBillingReports, HuntressSIEMRequestParams],
    IPaginateable[SIEMBillingReports, HuntressSIEMRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "billing_reports", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SIEMBillingReports)
        IPaginateable.__init__(self, SIEMBillingReports)

    def id(self, id: int) -> BillingIdreportsEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized BillingIdreportsEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            BillingIdreportsEndpoint: The initialized BillingIdreportsEndpoint object.
        """
        child = BillingIdreportsEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSIEMRequestParams | None = None,
    ) -> PaginatedResponse[SIEMBillingReports]:
        """
        Performs a GET request against the /billing_reports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SIEMBillingReports]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["limit"] = limit
        else:
            params = {"page": page, "limit": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SIEMBillingReports,
            self,
            "billing_reports",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSIEMRequestParams | None = None,
    ) -> SIEMBillingReports:
        """
        Performs a GET request against the /billing_reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SIEMAuthInformation: The parsed response data.
        """
        return self._parse_many(
            SIEMBillingReports,
            super()._make_request("GET", data=data, params=params).json().get('billing_reports', {}),
        )
