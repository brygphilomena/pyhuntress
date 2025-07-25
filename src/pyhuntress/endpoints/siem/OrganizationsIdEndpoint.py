from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.siem import SIEMOrganizations
from pyhuntress.types import (
    JSON,
    HuntressSIEMRequestParams,
)


class OrganizationsIdEndpoint(
    HuntressEndpoint,
    IGettable[SIEMOrganizations, HuntressSIEMRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SIEMOrganizations)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSIEMRequestParams | None = None,
    ) -> SIEMOrganizations:
        """
        Performs a GET request against the /organizations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SIEMAuthInformation: The parsed response data.
        """
        return self._parse_one(
            SIEMOrganizations,
            super()._make_request("GET", data=data, params=params).json().get('organization', {}),
        )
