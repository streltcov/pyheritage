# -*- coding: utf-8 -*-

"""Dublin Core base classes;

"""


from typing import Callable

from pydantic import ConfigDict

from pyheritage.cidoc.base import Identity


__all__ = ('DCEntityBase', 'dc_element', )


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
        DC_ENTITY_REGISTRY[label] = cls.__class__

        return cls

    return wrapper
