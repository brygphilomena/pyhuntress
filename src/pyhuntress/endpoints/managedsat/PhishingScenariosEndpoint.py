from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.PhishingScenariosIdEndpoint import PhishingScenariosIdEndpoint
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


class PhishingScenariosEndpoint(
    HuntressEndpoint,
    IGettable[SATPhishingScenarios, HuntressSATRequestParams],
    IPaginateable[SATPhishingScenarios, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "phishing-scenarios", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATPhishingScenarios)
        IPaginateable.__init__(self, SATPhishingScenarios)

    def id(self, id: int) -> PhishingScenariosIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized PhishingScenariosIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            PhishingScenariosIdEndpoint: The initialized PhishingScenariosIdEndpoint object.
        """
        child = PhishingScenariosIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATPhishingScenarios]:
        """
        Performs a GET request against the /phishing-scenarios endpoitments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATPhishingScenarios]: The initialized PaginatedResponse object.
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
        Performs a GET request against the /phishing-scenarios endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATGroups: The parsed response data.
        """
        return self._parse_many(
            SATPhishingScenarios,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
