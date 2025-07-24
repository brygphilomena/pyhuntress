from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATLearnerActivities
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class AssignmentsIdLearnerActivityEndpoint(
    HuntressEndpoint,
    IGettable[SATLearnerActivities, HuntressSATRequestParams],
    IPaginateable[SATLearnerActivities, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "learner-activity", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATLearnerActivities)
        IPaginateable.__init__(self, SATLearnerActivities)

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATLearnerActivities]:
        """
        Performs a GET request against the /assignments/{id}/learner-activity endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATLearnerActivities]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SATLearnerActivities,
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
    ) -> SATLearnerActivities:
        """
        Performs a GET request against the /assignments/{id}/learner-activity endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATLearnerActivitiesInformation: The parsed response data.
        """
        return self._parse_many(
            SATLearnerActivities,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
