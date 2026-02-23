# -*- coding: utf-8 -*-

"""CIDOC CRM entities, representing primitive values (numbers, strings, spatial  etc.)

https://cidoc-crm.org/html/cidoc_crm_v7.0.html

"""


from __future__ import __annotations__  # noqa

from typing import Any, Optional

from edtf import EDTFObject
from pydantic import Field

from pyheritage.cidoc.core.base import CRMEntityBase, entity_register


__all__ = ('E59PrimitiveValue', 'E60Number', 'E61TimePrimitive', 'E62String', 'E94SpacePrimitive',
           'E95SpaceTimePrimitive', )


@entity_register(label='E59 Primitive Value')
class E59PrimitiveValue(CRMEntityBase):
    """'E59 Primitive Value' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E59
    Contains no values and serves only as a base class for other primitive value models;

    Attributes:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='E60 Number')
class E60Number(E59PrimitiveValue):
    """'E60 Number' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E60
    Extends E59PrimitiveValue and contains a single numeric field;

    Attributes:
        value (str): numeric (int or float) value, default to 0;

    """

    value: int | float = Field(default=0)

    # ------------------------------ #

    def __repr__(self) -> str:
        return f'E60({self.value})'


# ******************************************************************************************************************* #


@entity_register(label='E61 Time Primitive')
class E61TimePrimitive(E59PrimitiveValue):
    """'E61 Primitive Value' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E61
    Extends E59PrimitiveValue and contains a single numeric field (defaults to 0);

    """

    value: str = Field(default='')
    _parsed: Optional[EDTFObject] = Field(default=None, exclude=True, repr=False, description='Cached parsing result'
                                                                                              ' (not serialized)')

    # ------------------------------ #

    @property
    def parsed(self) -> Optional[Any]:
        """Parsed EDTF value;

        """
        return self._parsed

    # ------------------------------ #

    def __repr__(self) -> str:
        return f'E61({self.value})'


# ******************************************************************************************************************* #


@entity_register(label='E62 String')
class E62String(E59PrimitiveValue):
    """'E62 String' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E62
    Subclass of E59PrimitiveValue;
    Contains a single field - string value - a sequence of characters with optional language label;

    Language label allows to contain multilanguage values;

    Attributes:
        value (str)
        language (str): optional language label;

    """

    value: str = ''
    language: Optional[str] = Field(default=None)

    # ------------------------------ #

    def __str__(self) -> str:
        return self.value

    # ------------------------------ #

    def __repr__(self) -> str:
        language = f'{self.value} - {self.language}' if self.language else f'{self.value}'

        return f'E62({self.value}) {language}'


# ******************************************************************************************************************* #


@entity_register(label='E94 Space Primitive')
class E94SpacePrimitive(E59PrimitiveValue):
    """'E94 Space Primitive' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E94

    Spatial primitive - a machine-readable definition of a location or area;
    Supports two input formats - WKT and GeoJSON;

    Attributes:
        value (str): geometry;
        srs (str): optional EPSG code for spatial reference system;

    """

    value: str = Field(default='')
    srs: str = Field(default='ESPG:4326', description='Spatial Reference System (EPSG Code)')

    # ------------------------------ #

    def __repr__(self) -> str:
        return f'{self.value}'


# ******************************************************************************************************************* #


@entity_register(label='E95 SpaceTime Primitive')
class E95SpaceTimePrimitive(E59PrimitiveValue):
    """'E95 SpaceTime Primitive' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E95

    Attributes:
        spatial (E94SpacePrimitive)
        temporal (E61TimePrimitive)

    """

    spatial: Optional[E94SpacePrimitive] = None
    temporal: Optional[E61TimePrimitive] = None

    # ------------------------------ #

    def __repr__(self) -> str:
        return f'{self.spatial.value}'
