from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.siem import SIEMReports
from pyhuntress.types import (
    JSON,
    HuntressSIEMRequestParams,
)


class ReportsEndpoint(
    HuntressEndpoint,
    IGettable[SIEMReports, HuntressSIEMRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "reports", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SIEMReports)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSIEMRequestParams | None = None,
    ) -> SIEMReports:
        """
        Performs a GET request against the /Reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SIEMAuthInformation: The parsed response data.
        """
        return self._parse_many(
            SIEMReports,
            super()._make_request("GET", data=data, params=params).json().get('reports', {}),
        )
