# -*- coding: utf-8 -*-

"""CIDOC base classes;

"""


import uuid
from abc import ABC

from pydantic import BaseModel, ConfigDict, Field


__all__ = ('CRMEntityBase', 'PropertyMixin', 'entity_register', )


ENTITY_REGISTRY: dict[str, type] = {}


class PropertyMixin(ABC, BaseModel):
    """Base class for property mixin classes;

    """


# ******************************************************************************************************************* #


class Identity(ABC, BaseModel):
    """Node identification - not a CRM-class;

    """

    id: str = Field(
        default_factory=lambda: f"{uuid.uuid4()}",
        alias="@id",
        description="Node identifier, not a CRM-property"
    )


# ******************************************************************************************************************* #


class CRMEntityBase(Identity):
    """CIDOC CRM entities base class;

    """

    model_config = ConfigDict(
        extra='allow',
    )


# ******************************************************************************************************************* #


def entity_register(label: str) -> callable:
    """Entity decorator;

    Adds entity class to entity registry;
    Adds CRM code and CRM label to entity class attributes;

    """
    def wrapper(cls: CRMEntityBase) -> CRMEntityBase:
        code = label.split(" ")[0]
        cls.crm_code = code
        cls.crm_label = label
        ENTITY_REGISTRY[code] = cls.__class__

        return cls

    return wrapper
