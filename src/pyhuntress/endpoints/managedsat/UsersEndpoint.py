from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.UsersIdEndpoint import UsersIdEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyhuntress.models.managedsat import SATUsers
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class UsersEndpoint(
    HuntressEndpoint,
    IGettable[SATUsers, HuntressSATRequestParams],
#    IPostable[SATUsers, HuntressSATRequestParams],
    IPaginateable[SATUsers, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "users", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATUsers)
        IPaginateable.__init__(self, SATUsers)

    def id(self, id: int) -> UsersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized UsersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            UsersIdEndpoint: The initialized UsersIdEndpoint object.
        """
        child = UsersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATUsers]:
        """
        Performs a GET request against the /users endpoint and returns an initialized PaginatedResponse object.

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
            SATUsers,
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
    ) -> SATUsers:
        """
        Performs a GET request against the /users endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATAccountInformation: The parsed response data.
        """
        return self._parse_many(
            SATUsers,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )

#    def post(self, data: JSON | None = None, params: HuntressSATRequestParams | None = None) -> SATUsers:
#        """
#        Performs a POST request against the /company/companies endpoint.
#
#        Parameters:
#            data (dict[str, Any]): The data to send in the request body.
#            params (dict[str, int | str]): The parameters to send in the request query string.
#        Returns:
#            SATUsers: The parsed response data.
#        """
#        return self._parse_one(SATUsers, super()._make_request("POST", data=data, params=params).json())
