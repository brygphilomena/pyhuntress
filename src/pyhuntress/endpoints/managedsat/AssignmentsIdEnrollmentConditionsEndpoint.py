from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.managedsat import SATAssignments
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class AssignmentsIdEnrollmentConditionsEndpoint(
    HuntressEndpoint,
    IGettable[SATAssignments, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "enrollment-conditions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATAssignments)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSATRequestParams | None = None,
    ) -> SATAssignments:
        
        # TODO: Make this require the learnerid as a parameter
        
        """
        Performs a GET request against the /assignments/{id}/enrollment-conditions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATAssignmentsInformation: The parsed response data.
        """
        return self._parse_many(
            SATAssignments,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
