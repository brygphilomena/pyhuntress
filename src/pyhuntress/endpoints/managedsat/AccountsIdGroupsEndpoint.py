from pyhuntress.endpoints.base.huntress_endpoint import HuntressEndpoint
from pyhuntress.interfaces import (
    IGettable,
)
from pyhuntress.models.managedsat import SATGroups
from pyhuntress.types import (
    JSON,
    HuntressSATRequestParams,
)


class AccountsIdGroupsEndpoint(
    HuntressEndpoint,
    IGettable[SATGroups, HuntressSATRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        HuntressEndpoint.__init__(self, client, "groups", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SATGroups)

    def get(
        self,
        data: JSON | None = None,
        params: HuntressSATRequestParams | None = None,
    ) -> SATGroups:
        
        # TODO: Make this require the learnerid as a parameter
        
        """
        Performs a GET request against the /accounts/{id}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SATGroups: The parsed response data.
        """
        return self._parse_many(
            SATGroups,
            super()._make_request("GET", data=data, params=params).json().get('data', {}),
        )
