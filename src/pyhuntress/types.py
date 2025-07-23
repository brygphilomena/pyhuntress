from typing import Literal, TypeAlias

from typing_extensions import NotRequired, TypedDict
from datetime import datetime

Literals: TypeAlias = str | int | float | bool
JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | Literals | None


class Patch(TypedDict):
    op: Literal["add"] | Literal["replace"] | Literal["remove"]
    path: str
    value: JSON


class HuntressSATRequestParams(TypedDict):
    conditions: NotRequired[str]
    childConditions: NotRequired[str]
    customFieldConditions: NotRequired[str]
    orderBy: NotRequired[str]
    page: NotRequired[int]
    pageSize: NotRequired[int]
    fields: NotRequired[str]
    columns: NotRequired[str]


class HuntressSIEMRequestParams(TypedDict):
    created_at_min: NotRequired[datetime]
    created_at_max: NotRequired[datetime]
    updated_at_min: NotRequired[datetime]
    updated_at_min: NotRequired[datetime]
    customFieldConditions: NotRequired[str]
    page_token: NotRequired[str]
    page: NotRequired[int]
    limit: NotRequired[int]
    organization_id: NotRequired[int]
    platform: NotRequired[str]
    status: NotRequired[str]
    indicator_type: NotRequired[str]
    severity: NotRequired[str]
    platform: NotRequired[str]
    agent_id: NotRequired[str]
    type: NotRequired[str]
    entity_id: NotRequired[int]
    types: NotRequired[str]
    statuses: NotRequired[str]


GenericRequestParams: TypeAlias = dict[str, Literals]
RequestParams: TypeAlias = HuntressSATRequestParams | HuntressSIEMRequestParams | GenericRequestParams
PatchRequestData: TypeAlias = list[Patch]
RequestData: TypeAlias = JSON | PatchRequestData
RequestMethod: TypeAlias = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
