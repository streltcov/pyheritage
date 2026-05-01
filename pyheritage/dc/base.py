# -*- coding: utf-8 -*-

"""Dublin Core base classes;

"""


from typing import Callable, Optional

from pydantic import ConfigDict

from pyheritage.cidoc.base import Identity


__all__ = ('DCEntityBase', 'dc_element', 'DCDescription', )


DC_ENTITY_REGISTRY: dict[str, type] = {}


class DCEntityBase(Identity):
    """Dublin Core entity base class;

    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )


# ******************************************************************************************************************* #


def dc_element(label: str) -> Callable:
    """Dublin Core element decorator;

    Adds element class to entity registry;
    Adds DC label to element class attributes;

    """
    def wrapper(cls: DCEntityBase) -> DCEntityBase:
        cls.dc_label = label
        DC_ENTITY_REGISTRY[label] = cls

        return cls

    return wrapper


# ******************************************************************************************************************* #


class DCDescription(DCEntityBase):
    """Dublin Core resource description model;

    Aggregates multiple DC elements into a single resource description;

    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    title: Optional[list[str]] = None
    creator: Optional[list[str]] = None
    subject: Optional[list[str]] = None
    description: Optional[list[str]] = None
    publisher: Optional[list[str]] = None
    contributor: Optional[list[str]] = None
    date: Optional[list[str]] = None
    type: Optional[list[str]] = None
    format: Optional[list[str]] = None
    identifier: Optional[list[str]] = None
    source: Optional[list[str]] = None
    language: Optional[list[str]] = None
    relation: Optional[list[str]] = None
    coverage: Optional[list[str]] = None
    rights: Optional[list[str]] = None
