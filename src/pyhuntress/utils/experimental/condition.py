from __future__ import annotations

import inspect
import re
from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from pyhuntress.utils.naming import to_camel_case

if TYPE_CHECKING:
    from collections.abc import Callable

T = TypeVar("T")


class ValueType(Enum):
    STR = 1
    INT = 2
    DATETIME = 3


class Condition(Generic[T]):
    def __init__(self: Condition[T]) -> None:
        self._condition_string: str = ""
        self._field = ""

    def field(self: Condition[T], selector: Callable[[type[T]], Any]) -> Condition[T]:
        field = ""

        frame = inspect.currentframe()
        try:
            context = inspect.getframeinfo(frame.f_back).code_context
            caller_lines = "".join([line.strip() for line in context])
            m = re.search(r"field\s*\(([^)]+)\)", caller_lines)
            if m:
                caller_lines = m.group(1)

            field = to_camel_case("/".join(caller_lines.replace("(", "").replace(")", "").split(".")[1:]))

        finally:
            del frame

        self._condition_string += field
        return self

    def equals(self: Condition[T], value: Any) -> Condition[T]:  # noqa: ANN401
        self._condition_string += " = "
        self.__add_typed_value_to_string(value, type(value))
        return self

    def not_equals(self: Condition[T], value: Any) -> Condition[T]:  # noqa: ANN401
        self._condition_string += " = "
        self.__add_typed_value_to_string(value, type(value))
        return self

    def less_than(self: Condition[T], value: Any) -> Condition[T]:  # noqa: ANN401
        self._condition_string += " < "
        self.__add_typed_value_to_string(value, type(value))
        return self

    def less_than_or_equals(
        self: Condition[T],
        value: Any,  # noqa: ANN401
    ) -> Condition[T]:
        self._condition_string += " <= "
        self.__add_typed_value_to_string(value, type(value))
        return self

    def greater_than(self: Condition[T], value: Any) -> Condition[T]:  # noqa: ANN401
        self._condition_string += " > "
        self.__add_typed_value_to_string(value, type(value))
        return self

    def greater_than_or_equals(
        self: Condition[T],
        value: Any,  # noqa: ANN401
    ) -> Condition[T]:
        self._condition_string += " >= "
        self.__add_typed_value_to_string(value, type(value))
        return self

    def contains(self: Condition[T], value: Any) -> Condition[T]:  # noqa: ANN401
        self._condition_string += " CONTAINS "
        self.__add_typed_value_to_string(value, type(value))
        return self

    def like(self: Condition[T], value: Any) -> Condition[T]:  # noqa: ANN401
        self._condition_string += " LIKE "
        self.__add_typed_value_to_string(value, type(value))
        return self

    def in_(self: Condition[T], value: Any) -> Condition[T]:  # noqa: ANN401
        self._condition_string += " IN "
        self.__add_typed_value_to_string(value, type(value))
        return self

    def not_(self: Condition[T], value: Any) -> Condition[T]:  # noqa: ANN401
        self._condition_string += " NOT "
        self.__add_typed_value_to_string(value, type(value))
        return self

    def __add_typed_value_to_string(  # noqa: ANN202
        self: Condition[T],
        value: Any,  # noqa: ANN401
        type: type,  # noqa: A002
    ):
        if type is str:
            self._condition_string += f'"{value}"'
        elif type is int:  # noqa: SIM114
            self._condition_string += str(value)
        elif type is bool:
            self._condition_string += str(value)
        elif type is datetime:
            self._condition_string += f"[{value}]"
        else:
            self._condition_string += f'"{value}"'

    def and_(self: Condition[T], selector: Callable[[type[T]], Any] | None = None) -> Condition[T]:
        self._condition_string += " AND "

        if selector is not None:
            field = ""
            frame = inspect.currentframe()
            try:
                context = inspect.getframeinfo(frame.f_back).code_context
                caller_lines = "".join([line.strip() for line in context])
                m = re.search(r"and_\s*\(([^)]+)\)", caller_lines)
                if m:
                    caller_lines = m.group(1)

                field = "/".join(caller_lines.replace("(", "").replace(")", "").split(".")[1:])

            finally:
                del frame

            self._condition_string += field
        return self

    def or_(self: Condition[T], selector: Callable[[type[T]], Any] | None = None) -> Condition[T]:
        self._condition_string += " OR "

        if selector is not None:
            field = ""
            frame = inspect.currentframe()
            try:
                context = inspect.getframeinfo(frame.f_back).code_context
                caller_lines = "".join([line.strip() for line in context])
                m = re.search(r"or_\s*\(([^)]+)\)", caller_lines)
                if m:
                    caller_lines = m.group(1)

                field = "/".join(caller_lines.replace("(", "").replace(")", "").split(".")[1:])

            finally:
                del frame

            self._condition_string += field
        return self

    def wrap(self: Condition[T], condition: Callable[[Condition[T]], Condition[T]]) -> Condition[T]:
        self._condition_string += f"({condition(Condition[T]())})"
        return self

    def __str__(self: Condition[T]) -> str:
        return self._condition_string.strip()
