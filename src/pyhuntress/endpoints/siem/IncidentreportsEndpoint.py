from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.siem.IncidentreportsIdEndpoint import IncidentreportsIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.siem import SIEMIncidentReports
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSIEMRequestParams,
)


class IncidentreportsEndpoint(
    HuntressEndpoint,
    IGettable[SIEMIncidentReports, HuntressSIEMRequestParams],
    IPaginateable[SIEMIncidentReports, HuntressSIEMRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "incident_reports", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SIEMIncidentReports)
        IPaginateable.__init__(self, SIEMIncidentReports)

    def id(self, id: int) -> IncidentreportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized IncidentreportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            IncidentreportsIdEndpoint: The initialized IncidentreportsIdEndpoint object.
        """
        child = IncidentreportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSIEMRequestParams | None = None,
    ) -> PaginatedResponse[SIEMIncidentReports]:
        """
        Performs a GET request against the /incident_reports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SIEMIncidentReports]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["limit"] = limit
        else:
            params = {"page": page, "limit": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SIEMIncidentReports,
            self,
            "incident_reports",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSIEMRequestParams | None = None,
    ) -> SIEMIncidentReports:
        """
        Performs a GET request against the /incident_reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SIEMAuthInformation: The parsed response data.
        """
        return self._parse_many(
            SIEMIncidentReports,
            super()._make_request("GET", data=data, params=params).json().get('incident_reports', {}),
        )
