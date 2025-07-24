import json
from typing import ClassVar
from urllib.parse import urlsplit, urlunsplit

from requests import JSONDecodeError, Response


class HuntressException(Exception):
    _code_explanation: ClassVar[str] = ""  # Ex: for 404 "Not Found"
    _error_suggestion: ClassVar[str] = ""  # Ex: for 404 "Check the URL you are using is correct"

    def __init__(self, req_response: Response, *, extra_message: str = "") -> None:
        self.response = req_response
        self.extra_message = extra_message
        super().__init__(self.message())

    def _get_sanitized_url(self) -> str:
        """
        Simplify URL down to method, hostname, and path.
        """
        url_components = urlsplit(self.response.url)
        return urlunsplit(
            (
                url_components.scheme,
                url_components.hostname,
                url_components.path,
                "",
                "",
            )
        )

    def details(self) -> str:
        try:
            # If response was json, then format it nicely
            return json.dumps(self.response.json(), indent=4)
        except JSONDecodeError:
            return self.response.text

    def message(self) -> str:
        return (
            f"A HTTP {self.response.status_code} ({self._code_explanation}) error has occurred while requesting"
            f" {self._get_sanitized_url()}.\n{self.response.reason}\n{self._error_suggestion}\n{self.extra_message}"
        ).strip()  # Remove extra whitespace (Ex: if extra_message == "")


class MalformedRequestException(HuntressException):
    _code_explanation = "Bad Request"
    _error_suggestion = (
        "The request could not be understood by the server due to malformed syntax. Please check modify your request"
        " before retrying."
    )


class AuthenticationFailedException(HuntressException):
    _code_explanation = "Unauthorized"
    _error_suggestion = "Please check your credentials are correct before retrying."


class PermissionsFailedException(HuntressException):
    _code_explanation = "Forbidden"
    _error_suggestion = "You may be attempting to access a resource you do not have the appropriate permissions for."


class NotFoundException(HuntressException):
    _code_explanation = "Not Found"
    _error_suggestion = "You may be attempting to access a resource that has been moved or deleted."


class MethodNotAllowedException(HuntressException):
    _code_explanation = "Method Not Allowed"
    _error_suggestion = "This resource does not support the HTTP method you are trying to use."


class ConflictException(HuntressException):
    _code_explanation = "Conflict"
    _error_suggestion = "This resource is possibly in use or conflicts with another record."


class ServerError(HuntressException):
    _code_explanation = "Internal Server Error"


class ObjectExistsError(HuntressException):
    _code_explanation = "Object Exists"
    _error_suggestion = "This resource already exists."
