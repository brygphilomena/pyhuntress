from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.endpoints.managedsat.AssignmentsIdLearnersEndpoint import AssignmentsIdLearnersEndpoint
from pyhuntress.endpoints.managedsat.AssignmentsIdLearnerActivityEndpoint import AssignmentsIdLearnerActivityEndpoint
from pyhuntress.endpoints.managedsat.AssignmentsIdCompletionCertificateEndpoint import AssignmentsIdCompletionCertificateEndpoint
from pyhuntress.endpoints.managedsat.AssignmentsIdEnrollmentConditionsEndpoint import AssignmentsIdEnrollmentConditionsEndpoint
from pyhuntress.endpoints.managedsat.AssignmentsIdEnrollmentExtrasEndpoint import AssignmentsIdEnrollmentExtrasEndpoint
from pyhuntress.interfaces import (
    IGettable,
    IPaginateable,
)
from pyhuntress.models.managedsat import SATAssignments
from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class AssignmentsIdEndpoint(
    HuntressEndpoint,
    IGettable[SATAssignments, HuntressSATRequestParams],
    IPaginateable[SATAssignments, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATAssignments)
        IPaginateable.__init__(self, SATAssignments)

        self.learners = self._register_child_endpoint(AssignmentsIdLearnersEndpoint(client, parent_endpoint=self))
        self.learner_activity = self._register_child_endpoint(AssignmentsIdLearnerActivityEndpoint(client, parent_endpoint=self))
        self.completion_certificate = self._register_child_endpoint(AssignmentsIdCompletionCertificateEndpoint(client, parent_endpoint=self))
        self.enrollment_conditions = self._register_child_endpoint(AssignmentsIdEnrollmentConditionsEndpoint(client, parent_endpoint=self))
        self.enrollment_extras = self._register_child_endpoint(AssignmentsIdEnrollmentExtrasEndpoint(client, parent_endpoint=self))

    def paginated(
        self,
        page: int,
        limit: int,
        params: HuntressSATRequestParams | None = None,
    ) -> PaginatedResponse[SATAssignments]:
        """
        Performs a GET request against the /assignments/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SATAssignments]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SATAssignments,
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
    ) -> SATAssignments:
        """
        Performs a GET request against the /assignments/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATAssignmentsInformation: The parsed response data.
        """
        return self._parse_one(
            SATAssignments,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
