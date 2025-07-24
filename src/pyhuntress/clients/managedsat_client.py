import typing
from datetime import datetime, timedelta, timezone

from pyhuntress.clients.huntress_client import HuntressClient
from pyhuntress.config import Config

if typing.TYPE_CHECKING:
    from pyhuntress.endpoints.managedsat.AccountsEndpoint import AccountsEndpoint
    from pyhuntress.endpoints.managedsat.UsersEndpoint import UsersEndpoint
    from pyhuntress.endpoints.managedsat.AssignmentsEndpoint import AssignmentsEndpoint
    from pyhuntress.endpoints.managedsat.EpisodesEndpoint import EpisodesEndpoint
    from pyhuntress.endpoints.managedsat.DepartmentsEndpoint import DepartmentsEndpoint
    from pyhuntress.endpoints.managedsat.GroupsEndpoint import GroupsEndpoint
    from pyhuntress.endpoints.managedsat.LearnersEndpoint import LearnersEndpoint
    from pyhuntress.endpoints.managedsat.PhishingCampaignsEndpoint import PhishingCampaignsEndpoint
    from pyhuntress.endpoints.managedsat.PhishingCampaignScenariosEndpoint import PhishingCampaignScenariosEndpoint
    from pyhuntress.endpoints.managedsat.PhishingAttemptsEndpoint import PhishingAttemptsActionsEndpoint
    from pyhuntress.endpoints.managedsat.PhishingScenariosEndpoint import PhishingScenariosEndpoint


class ManagedSATCodebaseError(Exception):
    def __init__(self) -> None:
        super().__init__("Could not retrieve codebase from API.")


class HuntressSATAPIClient(HuntressClient):
    """
    Huntress Managed SAT API client. Handles the connection to the Huntress Managed SAT API
    and the configuration of all the available endpoints.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        api_scopes: str,
    ) -> None:
        """
        Initializes the client with the given credentials.

        Parameters:
            client_id (str): URL of the Huntress Managed SAT client id.
            client_secret (str): Your Huntress Managed SAT API client secret.
            api_scopes (str): Your Huntress Managed SAT API scope.
        """
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self.api_scopes: str = api_scopes
        self.token_expiry_time: datetime = datetime.now(tz=timezone.utc)

        # Grab first access token
        self.access_token: str = self._get_access_token()

    # Initializing endpoints
    @property
    def accounts(self) -> "AccountsEndpoint":
        from pyhuntress.endpoints.managedsat.AccountsEndpoint import AccountsEndpoint

        return AccountsEndpoint(self)

    @property
    def users(self) -> "UsersEndpoint":
        from pyhuntress.endpoints.managedsat.UsersEndpoint import UsersEndpoint

        return UsersEndpoint(self)

    @property
    def assignments(self) -> "AssignmentsEndpoint":
        from pyhuntress.endpoints.managedsat.AssignmentsEndpoint import AssignmentsEndpoint

        return AssignmentsEndpoint(self)

    @property
    def episodes(self) -> "EpisodesEndpoint":
        from pyhuntress.endpoints.managedsat.EpisodesEndpoint import EpisodesEndpoint

        return EpisodesEndpoint(self)

    @property
    def departments(self) -> "DepartmentsEndpoint":
        from pyhuntress.endpoints.managedsat.DepartmentsEndpoint import DepartmentsEndpoint

        return DepartmentsEndpoint(self)

    @property
    def groups(self) -> "GroupsEndpoint":
        from pyhuntress.endpoints.managedsat.GroupsEndpoint import GroupsEndpoint

        return GroupsEndpoint(self)

    @property
    def learners(self) -> "LearnersEndpoint":
        from pyhuntress.endpoints.managedsat.LearnersEndpoint import LearnersEndpoint

        return LearnersEndpoint(self)

    @property
    def phishing_campaigns(self) -> "PhishingCampaignsEndpoint":
        from pyhuntress.endpoints.managedsat.PhishingCampaignsEndpoint import PhishingCampaignsEndpoint

        return PhishingCampaignsEndpoint(self)

    @property
    def phishing_campaign_scenarios(self) -> "PhishingCampaignScenariosEndpoint":
        from pyhuntress.endpoints.managedsat.PhishingCampaignScenariosEndpoint import PhishingCampaignScenariosEndpoint

        return PhishingCampaignScenariosEndpoint(self)

    @property
    def phishing_attempts(self) -> "PhishingAttemptsActionsEndpoint":
        from pyhuntress.endpoints.managedsat.PhishingAttemptsActionsEndpoint import PhishingAttemptsActionsEndpoint

        return PhishingAttemptsActionsEndpoint(self)

    @property
    def phishing_scenarios(self) -> "PhishingScenariosEndpoint":
        from pyhuntress.endpoints.managedsat.PhishingScenariosEndpoint import PhishingScenariosEndpoint

        return PhishingScenariosEndpoint(self)

    def _get_url(self) -> str:
        """
        Generates and returns the URL for the Huntress Managed SAT API endpoints based on the company url and codebase.
        This only still exists incase Huntress eventually moves to some client specific URL format
        Returns:
            str: API URL.
        """
        return f"https://mycurricula.com/api/v1"

    def _get_access_token(self) -> str:
        """
        Performs a request to the ConnectWise Automate API to obtain an access token.
        """
        token_url = self._get_url().replace("api/v1", "oauth/token") #strip the API endpoints to use the oauth token url
        auth_response = self._make_request(
            "POST",
            token_url,
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": self.api_scopes
                },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"
                },
        )
        auth_resp_json = auth_response.json()
        token = auth_resp_json["access_token"]
        expires_in_sec = auth_resp_json["expires_in"]
        self.token_expiry_time = datetime.now(tz=timezone.utc) + timedelta(seconds=expires_in_sec)
        return token

    def _refresh_access_token_if_necessary(self):
        if datetime.now(tz=timezone.utc) > self.token_expiry_time:
            self.access_token = self._get_access_token()

    def _get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        self._refresh_access_token_if_necessary()
        return {
            "Content-Type": "application/vnd.api+json",
            "Accept": "application/vnd.api+json",
            "Authorization": f"Bearer {self.access_token}",
        }
