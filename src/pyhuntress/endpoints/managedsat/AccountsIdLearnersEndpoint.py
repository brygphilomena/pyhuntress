from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.managedsat import SATLearners
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class AccountsIdLearnersEndpoint(
    HuntressEndpoint,
    IGettable[SATLearners, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "learners", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATLearners)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSATRequestParams | None = None,
    ) -> SATLearners:
        
        # TODO: Make this require the learnerid as a parameter
        
        """
        Performs a GET request against the /accounts/{id}/learners endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATGSATLearnersroups: The parsed response data.
        """
        return self._parse_many(
            SATLearners,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
