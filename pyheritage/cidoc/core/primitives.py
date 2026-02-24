# -*- coding: utf-8 -*-

"""CIDOC CRM entities, representing primitive values (numbers, strings, spatial  etc.)

https://cidoc-crm.org/html/cidoc_crm_v7.0.html

"""


from __future__ import __annotations__  # noqa

import re
from enum import Enum
from typing import Any, Optional, Self

from edtf import EDTFObject, parse_edtf, text_to_edtf
from edtf.parser.edtf_exceptions import EDTFParseException
from pydantic import Field, field_validator

from pyheritage.cidoc.core.base import CRMEntityBase, entity_register


__all__ = ('E59PrimitiveValue', 'E60Number', 'E61TimePrimitive', 'E62String', 'E94SpacePrimitive',
           'E95SpaceTimePrimitive', )


# ******************************************************************************************************************* #


class TimePrecision(str, Enum):
    """The accuracy level of the time primitive;

    It is determined by the python-edtf library or manually by the string format;

    """

    MILLENNIUM = "millennium"
    CENTURY = "century"
    DECADE = "decade"
    YEAR = "year"
    MONTH = "month"
    DAY = "day"
    DATETIME = "datetime"
    UNKNOWN = "unknown"


# ******************************************************************************************************************* #


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

    @property
    def precision(self) -> str:
        """Dynamic property - time primitive precision level;

        """
        if not self.value:
            return TimePrecision.UNKNOWN

        value = self.value.rstrip("~?%")

        if 'T' in value:
            return TimePrecision.DATETIME

        if 'xxx' in value:
            return TimePrecision.MILLENNIUM

        if 'xx' in value:
            return TimePrecision.CENTURY

        if 'x' in value:
            return TimePrecision.DECADE

        parts = value.lstrip("-").split("-")

        if len(parts) >= 3:
            return TimePrecision.DAY

        if len(parts) == 2:
            return TimePrecision.MONTH

        return TimePrecision.YEAR

    # ------------------------------ #

    @property
    def is_approximate(self) -> bool:
        """Dynamic property - checks if time primitive value is approximate;

        """
        return bool(self.value) and self.value[-1] in ("~", "%", )

    # ------------------------------ #

    @property
    def is_uncertain(self) -> bool:
        """Dynamic property - checks if time primitive value is uncertain;

        """
        return bool(self.value) and self.value[-1] in ("?", "%", )

    # ------------------------------ #

    @property
    def is_interval(self) -> bool:
        """Dynamic property - checks if time primitive value is time interval;

        """
        return "/" in self.value

    # ------------------------------ #

    @property
    def is_open(self) -> bool:
        """Dynamic property - checks if time primitive value is open;

        """
        return ".." in self.value

    # ------------------------------ #

    @property
    def is_bce(self) -> bool:
        """Dynamic property - checks if time primitive value is BCE;

        """
        return self.value.startswith('-')

    # ------------------------------ #

    @property
    def year(self) -> Optional[int]:
        """Dynamic property - year from EDTF time primitive;

        """
        if not self.value:
            return None

        value = self.value.split("/")[0].rstrip("~?%").replace("x", "0")
        match = re.match(r"^(-?\d+)", value)

        return int(match.group(1)) if match else None

    # ------------------------------ #

    @property
    def lower_strict(self) -> Optional[Any]:
        """Earliest possible date;

        """
        if self._parsed and hasattr(self._parsed, 'lower_strict'):
            return self._parsed.lower_strict()

        return None

    # ------------------------------ #

    @property
    def upper_strict(self) -> Optional[Any]:
        """Latest possible date;

        """
        if self._parsed and hasattr(self._parsed, 'upper_strict'):
            return self._parsed.upper_strict()

        return None

    # ------------------------------ #

    # @property
    # def sort_key(self) -> str:
    #     if self._parsed and hasattr(self._parsed, 'lower_strict'):
    #         try:
    #             ls = self._parsed.lower_strict()
    #             return f"{ls.tm_year:05d}-{ls.tm_mon:02d}-{ls.tm_mday:02d}"
    #         except Exception:
    #             pass
    #
    #     if not self.value:
    #         return ""
    #
    #     clean = self.value.split("/")[0].rstrip("~?%").replace("x", "0")
    #
    #     return clean

    # ------------------------------ #

    # ===== Factory methods =====

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
        extras = []

        if self.is_approximate: extras.append('≈')
        if self.is_uncertain: extras.append('?')
        if self.is_interval: extras.append('interval')
        suffix = f" [{','.join(extras)}]" if extras else ""

        return f'E61({self.value}{suffix})'


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
