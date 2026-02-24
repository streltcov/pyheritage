# -*- coding: utf-8 -*-

"""CIDOC CRM entities, representing primitive values (numbers, strings, spatial  etc.)

https://cidoc-crm.org/html/cidoc_crm_v7.0.html

"""


from __future__ import __annotations__  # noqa

from typing import Any, Optional, Self

from edtf import EDTFObject, parse_edtf, text_to_edtf
from edtf.parser.edtf_exceptions import EDTFParseException
from pydantic import Field, field_validator

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

    @classmethod
    @field_validator('value')
    def validate_edtf(cls, value: str) -> str:
        """Validation method for 'value' field;

        Args:
            value (str): EDTF time value to validate;

        """
        if not value:
            return value

        try:
            parse_edtf(value)
        except EDTFParseException:
            raise ValueError(
                f"Invalid EDTF value: '{value}'. "
                f"See https://www.loc.gov/standards/datetime/"
            )
        return value

    # ------------------------------ #

    def model_post_init(self, context: Any) -> None:  # noqa
        """Model post init method;

        """
        if self.value:
            try:
                object.__setattr__(self, '_parsed', parse_edtf(self.value))
            except EDTFParseException as e:
                raise ValueError(
                    f"Invalid EDTF value: {self.value}",
                    f"See https://www.loc.gov/standards/datetime",
                ) from e

    # ------------------------------ #

    @property
    def parsed(self) -> Optional[Any]:
        """Parsed EDTF value;

        """
        return self._parsed

    # ------------------------------ #

    @classmethod
    def from_text(cls, text: str) -> Self:
        """Creates E61 object from text description;

        Args:
            text (str): date in text format;

        Raises:
            ValueError - if the date couldn't be recognized from the text;

        """
        value = text_to_edtf(text)

        if value is None:
            raise ValueError(f'Unable to parse: {text}')

        return cls(value=value)

    # ------------------------------ #

    @classmethod
    def from_year(cls, year: int, approximate: bool = False) -> Self:
        """Creates E61 object from the numeric value of the year;

        Args:
            year (int): year (negative for BCE);
            approximate (bool): flag for approximate value;

        """
        value = f'{year:04d}' if year >= 0 else f'{-abs(year):04d}'

        if approximate:
            value += '~'

        return cls(value=value)

    # ------------------------------ #

    @classmethod
    def from_date(cls, year: int, month: int, day: int) -> Self:
        """Creates E81 object from date values;

        Args:
            year (int): numeric value for year;
            month (int): numeric value for month;
            day (int): numeric value for day;

        """
        prefix = f'{year:04d}' if year >= 0 else f'{-abs(year):04d}'
        value = f"{prefix}-{month:02d}-{day:02d}"

        return cls(value=value)

    # ------------------------------ #

    @classmethod
    def from_century(cls, century: int, approximate: bool = False) -> Self:
        """Creates E61 object from century value;

        from_century(16) -> 15xx" (century)";

        Args:
            century (int): century value;
            approximate (bool): flag for approximate value;

        """
        value = f"{century - 1:02d}xx"

        if approximate:
            value += '~'

        return cls(value=value)

    # ------------------------------ #

    @classmethod
    def from_decade(cls, start: int) -> Self:
        """Creates E61 object from decade value;

        from_decade(1950) -> "195x";

        Args:
            start (int): numeric value for decade;

        """
        value = f"{start // 10}x"

        return cls(value=value)

    # ------------------------------ #

    @classmethod
    def from_interval(cls, start: int, end: int) -> Self:
        """Creates E61 object from time interval;

        from_interval(1501, 1520) -> "1501/1520";

        Args:
            start (str): start value for time interval;
            end (str): end value for tim interval;

        """
        value = f"{start}/{end}"

        return cls(value=value)

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
