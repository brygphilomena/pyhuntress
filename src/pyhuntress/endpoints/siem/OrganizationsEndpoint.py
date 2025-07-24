from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.siem.OrganizationsIdEndpoint import OrganizationsIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.siem import SIEMOrganizations
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSIEMRequestParams,
)


class OrganizationsEndpoint(
    HuntressEndpoint,
    IGettable[SIEMOrganizations, HuntressSIEMRequestParams],
    IPaginateable[SIEMOrganizations, HuntressSIEMRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "organizations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SIEMOrganizations)
        IPaginateable.__init__(self, SIEMOrganizations)

    def id(self, id: int) -> OrganizationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized OrganizationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            OrganizationsIdEndpoint: The initialized OrganizationsIdEndpoint object.
        """
        child = OrganizationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSIEMRequestParams | None = None,
    ) -> PaginatedResponse[SIEMOrganizations]:
        """
        Performs a GET request against the /organizations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SIEMOrganizations]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["limit"] = limit
        else:
            params = {"page": page, "limit": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SIEMOrganizations,
            self,
            "organizations",
            page,
            limit,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSIEMRequestParams | None = None,
    ) -> SIEMOrganizations:
        """
        Performs a GET request against the /Organizations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SIEMAuthInformation: The parsed response data.
        """
        return self._parse_many(
            SIEMOrganizations,
            super()._make_request("GET", data=data, params=params).json().get('organizations', {}),
        )
