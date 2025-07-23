from __future__ import annotations

import inspect
from types import UnionType
from typing import Union, get_args, get_origin

from pydantic import BaseModel, ConfigDict

from pyhuntress.utils.naming import to_camel_case


class HuntressModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel_case,
        populate_by_name=True,
        use_enum_values=True,
        protected_namespaces=(),
    )

    @classmethod
    def _get_field_names(cls) -> list[str]:
        field_names = []
        for v in cls.__fields__.values():
            was_model = False
            for arg in get_args(v.annotation):
                if inspect.isclass(arg) and issubclass(arg, HuntressModel):
                    was_model = True
                    field_names.extend([f"{v.alias}/{sub}" for sub in arg._get_field_names()])

            if not was_model:
                field_names.append(v.alias)

        return field_names

    @classmethod
    def _get_field_names_and_types(cls) -> dict[str, str]:  # noqa: C901
        field_names_and_types = {}
        for v in cls.__fields__.values():
            was_model = False
            field_type = "None"
            if get_origin(v.annotation) is UnionType or get_origin(v.annotation) is Union:
                for arg in get_args(v.annotation):
                    if inspect.isclass(arg) and issubclass(arg, HuntressModel):
                        was_model = True
                        for sk, sv in arg._get_field_names_and_types().items():
                            field_names_and_types[f"{v.alias}/{sk}"] = sv
                    elif arg is not None and arg.__name__ != "NoneType":
                        field_type = arg.__name__
            else:
                if inspect.isclass(v.annotation) and issubclass(v.annotation, HuntressModel):
                    was_model = True
                    for sk, sv in v.annotation._get_field_names_and_types().items():
                        field_names_and_types[f"{v.alias}/{sk}"] = sv
                elif v.annotation is not None and v.annotation.__name__ != "NoneType":
                    field_type = v.annotation.__name__

            if not was_model:
                field_names_and_types[v.alias] = field_type

        return field_names_and_types
