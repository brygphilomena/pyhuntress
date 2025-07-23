import base64
import typing

from pyhuntress.clients.huntress_client import HuntressClient
from pyhuntress.config import Config

if typing.TYPE_CHECKING:
    from pyhuntress.endpoints.managedsat.CompanyEndpoint import CompanyEndpoint
    from pyhuntress.endpoints.managedsat.ConfigurationsEndpoint import ConfigurationsEndpoint
    from pyhuntress.endpoints.managedsat.ExpenseEndpoint import ExpenseEndpoint
    from pyhuntress.endpoints.managedsat.FinanceEndpoint import FinanceEndpoint
    from pyhuntress.endpoints.managedsat.MarketingEndpoint import MarketingEndpoint
    from pyhuntress.endpoints.managedsat.ProcurementEndpoint import ProcurementEndpoint
    from pyhuntress.endpoints.managedsat.ProjectEndpoint import ProjectEndpoint
    from pyhuntress.endpoints.managedsat.SalesEndpoint import SalesEndpoint
    from pyhuntress.endpoints.managedsat.ScheduleEndpoint import ScheduleEndpoint
    from pyhuntress.endpoints.managedsat.ServiceEndpoint import ServiceEndpoint
    from pyhuntress.endpoints.managedsat.SystemEndpoint import SystemEndpoint
    from pyhuntress.endpoints.managedsat.TimeEndpoint import TimeEndpoint


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
        managedsat_url: str,
        public_key: str,
        private_key: str,
    ) -> None:
        """
        Initializes the client with the given credentials and optionally a specific codebase.
        If no codebase is given, it tries to get it from the API.

        Parameters:
            managedsat_url (str): URL of the Huntress Managed SAT instance.
            public_key (str): Your Huntress Managed SAT API Public key.
            private_key (str): Your Huntress Managed SAT API Private key.
        """
        self.managedsat_url: str = managedsat_url
        self.public_key: str = public_key
        self.private_key: str = private_key

    # Initializing endpoints
    @property
    def company(self) -> "CompanyEndpoint":
        from pyhuntress.endpoints.managedsat.CompanyEndpoint import CompanyEndpoint

        return CompanyEndpoint(self)

    @property
    def configurations(self) -> "ConfigurationsEndpoint":
        from pyhuntress.endpoints.managedsat.ConfigurationsEndpoint import ConfigurationsEndpoint

        return ConfigurationsEndpoint(self)

    @property
    def expense(self) -> "ExpenseEndpoint":
        from pyhuntress.endpoints.managedsat.ExpenseEndpoint import ExpenseEndpoint

        return ExpenseEndpoint(self)

    @property
    def finance(self) -> "FinanceEndpoint":
        from pyhuntress.endpoints.managedsat.FinanceEndpoint import FinanceEndpoint

        return FinanceEndpoint(self)

    @property
    def marketing(self) -> "MarketingEndpoint":
        from pyhuntress.endpoints.managedsat.MarketingEndpoint import MarketingEndpoint

        return MarketingEndpoint(self)

    @property
    def procurement(self) -> "ProcurementEndpoint":
        from pyhuntress.endpoints.managedsat.ProcurementEndpoint import ProcurementEndpoint

        return ProcurementEndpoint(self)

    @property
    def project(self) -> "ProjectEndpoint":
        from pyhuntress.endpoints.managedsat.ProjectEndpoint import ProjectEndpoint

        return ProjectEndpoint(self)

    @property
    def sales(self) -> "SalesEndpoint":
        from pyhuntress.endpoints.managedsat.SalesEndpoint import SalesEndpoint

        return SalesEndpoint(self)

    @property
    def schedule(self) -> "ScheduleEndpoint":
        from pyhuntress.endpoints.managedsat.ScheduleEndpoint import ScheduleEndpoint

        return ScheduleEndpoint(self)

    @property
    def service(self) -> "ServiceEndpoint":
        from pyhuntress.endpoints.managedsat.ServiceEndpoint import ServiceEndpoint

        return ServiceEndpoint(self)

    @property
    def system(self) -> "SystemEndpoint":
        from pyhuntress.endpoints.managedsat.SystemEndpoint import SystemEndpoint

        return SystemEndpoint(self)

    @property
    def time(self) -> "TimeEndpoint":
        from pyhuntress.endpoints.managedsat.TimeEndpoint import TimeEndpoint

        return TimeEndpoint(self)

    def _get_url(self) -> str:
        """
        Generates and returns the URL for the Huntress Managed SAT API endpoints based on the company url and codebase.

        Returns:
            str: API URL.
        """
        return f"https://{self.managedsat_url}/{self.codebase.strip('/')}/apis/3.0"

    def _try_get_codebase_from_api(self, managedsat_url: str, company_name: str, headers: dict[str, str]) -> str:
        """
        Tries to retrieve the codebase from the API using the provided company url, company name and headers.

        Parameters:
            company_url (str): URL of the company.
            company_name (str): Name of the company.
            headers (dict[str, str]): Headers to be sent in the request.

        Returns:
            str: Codebase string or None if an error occurs.
        """
        url = f"https://{managedsat_url}/login/companyinfo/{company_name}"
        response = self._make_request("GET", url, headers=headers)
        return response.json().get("Codebase")

    def _get_auth_string(self) -> str:
        """
        Creates and returns the base64 encoded authorization string required for API requests.

        Returns:
            str: Base64 encoded authorization string.
        """
        return "Basic " + base64.b64encode(
            bytes(
                f"{self.company_name}+{self.public_key}:{self.private_key}",
                encoding="utf8",
            )
        ).decode("ascii")

    def _get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        return {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": self._get_auth_string(),
        }
