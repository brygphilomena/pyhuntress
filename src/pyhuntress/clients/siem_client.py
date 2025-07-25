import typing
from datetime import datetime, timezone
import base64

from pyhuntress.clients.huntress_client import HuntressClient
from pyhuntress.config import Config

if typing.TYPE_CHECKING:
    from pyhuntress.endpoints.siem.AccountEndpoint import AccountEndpoint
    from pyhuntress.endpoints.siem.ActorEndpoint import ActorEndpoint
    from pyhuntress.endpoints.siem.AgentsEndpoint import AgentsEndpoint
    from pyhuntress.endpoints.siem.BillingreportsEndpoint import BillingreportsEndpoint
    from pyhuntress.endpoints.siem.IncidentreportsEndpoint import IncidentreportsEndpoint
    from pyhuntress.endpoints.siem.OrganizationsEndpoint import OrganizationsEndpoint
    from pyhuntress.endpoints.siem.ReportsEndpoint import ReportsEndpoint
    from pyhuntress.endpoints.siem.SignalsEndpoint import SignalsEndpoint


class HuntressSIEMAPIClient(HuntressClient):
    """
    Huntress SIEM API client. Handles the connection to the Huntress SIEM API
    and the configuration of all the available endpoints.
    """

    def __init__(
        self,
        publickey: str,
        privatekey: str,
    ) -> None:
        """
        Initializes the client with the given credentials.

        Parameters:
            publickey (str): Your Huntress SIEM API public key.
            privatekey (str): Your Huntress SIEM API private key.
        """
        self.publickey: str = publickey
        self.privatekey: str = privatekey
        self.token_expiry_time: datetime = datetime.now(tz=timezone.utc)

        # Grab first access token
        self.base64_auth: str = self._get_auth_key()

    # Initializing endpoints
    @property
    def account(self) -> "AccountEndpoint":
        from pyhuntress.endpoints.siem.AccountEndpoint import AccountEndpoint

        return AccountEndpoint(self)

    @property
    def actor(self) -> "ActorEndpoint":
        from pyhuntress.endpoints.siem.ActorEndpoint import ActorEndpoint

        return ActorEndpoint(self)

    @property
    def agents(self) -> "AgentsEndpoint":
        from pyhuntress.endpoints.siem.AgentsEndpoint import AgentsEndpoint

        return AgentsEndpoint(self)

    @property
    def billing_reports(self) -> "BillingreportsEndpoint":
        from pyhuntress.endpoints.siem.BillingreportsEndpoint import BillingreportsEndpoint

        return BillingreportsEndpoint(self)

    @property
    def incident_reports(self) -> "IncidentreportsEndpoint":
        from pyhuntress.endpoints.siem.IncidentreportsEndpoint import IncidentreportsEndpoint

        return IncidentreportsEndpoint(self)

    @property
    def organizations(self) -> "OrganizationsEndpoint":
        from pyhuntress.endpoints.siem.OrganizationsEndpoint import OrganizationsEndpoint

        return OrganizationsEndpoint(self)

    @property
    def reports(self) -> "ReportsEndpoint":
        from pyhuntress.endpoints.siem.ReportsEndpoint import ReportsEndpoint

        return ReportsEndpoint(self)

    @property
    def signals(self) -> "SignalsEndpoint":
        from pyhuntress.endpoints.siem.SignalsEndpoint import SignalsEndpoint

        return SignalsEndpoint(self)

    def _get_url(self) -> str:
        """
        Generates and returns the URL for the Huntress SIEM API endpoints based on the company url and codebase.
        Logs in an obtains an access token.
        Returns:
            str: API URL.
        """
        return f"https://api.huntress.io/v1"

    def _get_auth_key(self) -> str:
        """
        Creates a base64 encoded authentication string to the Huntress SIEM API to obtain an access token.
        """
        # Format: base64encode(api_key:api_secret)
        
        auth_str = f"{self.publickey}:{self.privatekey}"
        auth_bytes = auth_str.encode('ascii')
        base64_auth = base64.b64encode(auth_bytes).decode('ascii')

        return base64_auth

    def _get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests. The access token is refreshed if necessary before returning.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        return {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.base64_auth}",
        }
