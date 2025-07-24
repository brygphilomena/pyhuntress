from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.managedsat import SATAssignmentsCompletionCertificates
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class AssignmentsIdCompletionCertificateEndpoint(
    HuntressEndpoint,
    IGettable[SATAssignmentsCompletionCertificates, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "completion-certificate", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATAssignmentsCompletionCertificates)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSATRequestParams | None = None,
    ) -> SATAssignmentsCompletionCertificates:
        
        # TODO: Make this require the learnerid as a parameter
        
        """
        Performs a GET request against the /assignments/{id}/completion-certificate endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATAssignmentsCompletionCertificatesInformation: The parsed response data.
        """
        return self._parse_one(
            SATAssignmentsCompletionCertificates,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
