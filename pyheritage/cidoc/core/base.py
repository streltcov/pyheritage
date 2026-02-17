# -*- coding: utf-8 -*-

"""CIDOC base classes;

"""


import uuid

from pydantic import BaseModel, ConfigDict, Field


class Identity(BaseModel):
    """Node identification - not a CRM-class;

    """

    _id: str = Field(
        default_factory=lambda: f"{uuid.uuid4()}",
        alias="@id",
        description="Node identifier, not a CRM-property"
    )


class CRMEntityBase(Identity):
    """CIDOC CRM entities base class;

    """

    model_config = ConfigDict(
        extra='allow',
    )
