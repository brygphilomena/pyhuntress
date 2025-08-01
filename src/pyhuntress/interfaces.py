from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar

from pyhuntress.responses.paginated_response import PaginatedResponse
from pyhuntress.types import (
    JSON,
    HuntressSIEMRequestParams,
    HuntressSATRequestParams,
    PatchRequestData,
)

if TYPE_CHECKING:
    from pydantic import BaseModel

TModel = TypeVar("TModel", bound="BaseModel")
TRequestParams = TypeVar(
    "TRequestParams",
    bound=HuntressSATRequestParams | HuntressSIEMRequestParams,
)


class IMethodBase(ABC, Generic[TModel, TRequestParams]):
    def __init__(self, model: TModel) -> None:
        self.model = model


class IPaginateable(IMethodBase, Generic[TModel, TRequestParams]):
    def __init__(self, model: TModel) -> None:
        super().__init__(model)

    @abstractmethod
    def paginated(
        self,
        page: int,
        page_size: int,
        params: TRequestParams | None = None,
    ) -> PaginatedResponse[TModel]:
        pass


class IGettable(IMethodBase, Generic[TModel, TRequestParams]):
    def __init__(self, model: TModel) -> None:
        super().__init__(model)

    @abstractmethod
    def get(
        self,
        data: JSON | None = None,
        params: TRequestParams | None = None,
    ) -> TModel:
        pass


class IPostable(IMethodBase, Generic[TModel, TRequestParams]):
    def __init__(self, model: TModel) -> None:
        super().__init__(model)

    @abstractmethod
    def post(
        self,
        data: JSON | None = None,
        params: TRequestParams | None = None,
    ) -> TModel:
        pass


class IPatchable(IMethodBase, Generic[TModel, TRequestParams]):
    def __init__(self, model: TModel) -> None:
        super().__init__(model)

    @abstractmethod
    def patch(
        self,
        data: PatchRequestData,
        params: TRequestParams | None = None,
    ) -> TModel:
        pass


class IPuttable(IMethodBase, Generic[TModel, TRequestParams]):
    def __init__(self, model: TModel) -> None:
        super().__init__(model)

    @abstractmethod
    def put(
        self,
        data: JSON | None = None,
        params: TRequestParams | None = None,
    ) -> TModel:
        pass


class IDeleteable(IMethodBase, Generic[TRequestParams]):
    def __init__(self, model: TModel) -> None:
        super().__init__(model)

    @abstractmethod
    def delete(
        self,
        data: JSON | None = None,
        params: TRequestParams | None = None,
    ) -> None:
        pass
