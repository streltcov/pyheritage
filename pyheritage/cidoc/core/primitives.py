# -*- coding: utf-8 -*-

"""CIDOC CRM entities, representing primitive values (numbers, strings, spatial  etc.)

https://cidoc-crm.org/html/cidoc_crm_v7.0.html

"""


from __future__ import annotations  # noqa

import json
import math
import re
from enum import Enum
from typing import Annotated, Any, Optional, Self

from edtf import EDTFObject, parse_edtf, text_to_edtf
from edtf.parser.edtf_exceptions import EDTFParseException
from pydantic import BeforeValidator, Field, field_validator, PrivateAttr
from pygeoif import from_wkt, shape

from pyheritage.cidoc.core.base import CRMEntityBase, entity_register


__all__ = ('E59PrimitiveValue', 'E60Number', 'E61TimePrimitive', 'E62String', 'E94SpacePrimitive',
           'E95SpaceTimePrimitive', 'CoercedNumber', 'CoercedTime', 'CoercedString', 'CoercedSpace', )


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


class SpatialFormat(str, Enum):
    """Supported spatial formats;

    Used by E94SpatialPrimitive entity model;

    """

    WKT = "wkt"
    GEOJSON = "geojson"
    UNKNOWN = "unknown"


# ******************************************************************************************************************* #


_WKT_PREFIX = re.compile(
    r"^\s*(POINT|LINESTRING|POLYGON|MULTIPOINT|MULTILINESTRING|"
    r"MULTIPOLYGON|GEOMETRYCOLLECTION)\s*[\(Z]",
    re.IGNORECASE,
)


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

    @classmethod
    @field_validator("value")
    def must_be_finite(cls, value: float | int) -> float | int:
        """Validation method for 'value' field;

        """
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError(f"E60 Number must be finite, got {value}")

        return value

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
    __parsed: Optional[EDTFObject] = PrivateAttr(default=None)

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
    def parsed(self) -> Optional[EDTFObject]:
        """Parsed EDTF object (python-edtf);

        """
        return self.__parsed

    # ------------------------------ #

    @property
    def precision(self) -> str:
        """Dynamic property - determine the level of temporal precision;

        Precision levels (defined in TimePrecision enum):
            * MILLENNIUM — "2xxx"
            * CENTURY — "15xx"
            * DECADE`` — "150x"
            * YEAR`` — "1503", "-0196"
            * MONTH — "1503-03"
            * DAY — "1503-03-15"
            * DATETIME — "1503-03-15T10:30:00"
            * UNKNOWN — empty string or unrecognized format

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
        """Whether the date is marked approximate;

        Examples:
            E61TimePrimitive("1703~").is_approximate     # True  (approximate)
            E61TimePrimitive("1703?").is_approximate     # False (uncertain, not approximate)
            E61TimePrimitive("1703").is_approximate      # False (exact)
            E61TimePrimitive("1703%").is_approximate     # True  (approximate + uncertain)


        """
        return bool(self.value) and self.value[-1] in ("~", "%", )

    # ------------------------------ #

    @property
    def is_uncertain(self) -> bool:
        """Whether the date is marked as uncertain;

        Examples:
            E61TimePrimitive("1703?").is_uncertain       # True  (uncertain)
            E61TimePrimitive("1703%").is_uncertain       # True  (uncertain + approximate)
            E61TimePrimitive("1703").is_uncertain        # False (exact)
            E61TimePrimitive("1703~").is_uncertain       # False (approximate, not uncertain)

        """
        return bool(self.value) and self.value[-1] in ("?", "%", )

    # ------------------------------ #

    @property
    def is_interval(self) -> bool:
        """Whether the value represents an EDTF interval;

        Examples:
            E61TimePrimitive("1703/1721").is_interval    # True
            E61TimePrimitive("1703/..").is_interval      # True
            E61TimePrimitive("../1721").is_interval      # True
            E61TimePrimitive("1703").is_interval         # False

        """
        return "/" in self.value

    # ------------------------------ #

    @property
    def is_open(self) -> bool:
        """Whether the value is an open-ended EDTF interval;

        Examples:
            E61TimePrimitive("1703/..").is_open          # True  (open end)
            E61TimePrimitive("../1721").is_open          # True  (open start)
            E61TimePrimitive("1703/1721").is_open        # False (closed interval)
            E61TimePrimitive("1703").is_open             # False (not an interval)

        """
        return ".." in self.value

    # ------------------------------ #

    @property
    def is_bce(self) -> bool:
        """Whether the date is before the Common Era;

        Examples:
            E61("-0196").is_bce             # True  (197 BCE)
            E61("-0001").is_bce             # True  (2 BCE)
            E61("0000").is_bce              # False (1 BCE in astronomical numbering)
            E61("1503").is_bce              # False
            E61("").is_bce                  # False

        """
        return self.value.startswith('-')

    # ------------------------------ #

    @property
    def year(self) -> Optional[int]:
        """Exact year from EDTF time primitive as an integer;

        Examples:
            E61TimePrimitive("1703").year                # 1703
            E61TimePrimitive("-0196").year               # -196
            E61TimePrimitive("2022-01-15").year          # 2024
            E61TimePrimitive("15xx").year                # 1500

        """
        if not self.value:
            return None

        value = self.value.split("/")[0].rstrip("~?%").replace("x", "0")
        match = re.match(r"^(-?\d+)", value)

        return int(match.group(1)) if match else None

    # ------------------------------ #

    @property
    def lower_strict(self) -> Optional[Any]:
        """Earliest possible date as time.struct_time;

        Delegates to edtf.lower_strict();

        Examples:
            E61TimePrimitive("17xx").lower_strict      # time.struct_time(tm_year=1700, tm_mon=1, tm_mday=1, ...)

        """
        if self.__parsed and hasattr(self.__parsed, 'lower_strict'):
            return self.__parsed.lower_strict()

        return None

    # ------------------------------ #

    @property
    def upper_strict(self) -> Optional[Any]:
        """Latest possible date as time.struct_time;

        Delegates to edtf.upper_strict();

        Examples:
            E61TimePrimitive("17xx").upper_strict      # time.struct_time(tm_year=1799, tm_mon=12, tm_mday=31, ...)

        """
        if self.__parsed and hasattr(self._parsed, 'upper_strict'):
            return self.__parsed.upper_strict()

        return None

    # ------------------------------ #

    @property
    def sort_key(self) -> str:
        """Normalized key for sorting and comparing dates;

        Transforms th EDTF value into a string suitable for correct lexicographic comparison;
        Used internally by dunder comparison operators and '__hash__' method;

        Note:
            This is a pragmatic simplified implementation

            * Intervals are compared by their start date;
            * Dates of different precision are compared by their lower bounds;
            * Approximate dates are treated as equal to exact dates;

        """
        if self.__parsed and hasattr(self.__parsed, 'lower_strict'):
            ls = self.__parsed.lower_strict()
            return f"{ls.tm_year:05d}-{ls.tm_mon:02d}-{ls.tm_mday:02d}"

        if not self.value:
            return ""

        clean = self.value.split("/")[0].rstrip("~?%").replace("x", "0")

        return clean

    # ------------------------------ #

    # ===== Comparison operators =====

    def __eq__(self, other) -> bool:  # noqa
        """Checks equality of two temporal primitives;

        Returns:
            True if both objects/values has the same 'sort_key' attribute;
            NotImplemented if type not supported;

        """
        if isinstance(other, E61TimePrimitive):
            return self.sort_key == other.sort_key

        return NotImplemented

    # ------------------------------ #

    def __lt__(self, other) -> bool:  # noqa
        """Checks if this time primitive is strictly earlier than another;

        Returns:
            True if this time primitive is earlier
            NotImplemented if type not supported;

        """
        if isinstance(other, E61TimePrimitive):
            return self.sort_key < other.sort_key

        return NotImplemented

    # ------------------------------ #

    def __le__(self, other) -> bool:  # noqa
        """Checks if this time primitive is earlier than or equal to another;

        Returns:
            True if current time primitive is earlier or equal;
            NotImplemented if type not supported;

        """
        if isinstance(other, E61TimePrimitive):
            return self == other or self < other

        return NotImplemented

    # ------------------------------ #

    def __gt__(self, other) -> bool:  # noqa
        """Checks if this time primitive is strictly later than another;

        Returns:
            True if current time primitive later;
            NotImplemented if type not supported;

        """
        if isinstance(other, E61TimePrimitive):
            return self.sort_key > other.sort_key

        return NotImplemented

    # ------------------------------ #

    def __ge__(self, other):  # noqa
        """Checks if this time primitive is later than or equal to another;

        Returns:
            True if current time primitive is later or equal;
            NotImplemented if type not supported;

        """
        if isinstance(other, E61TimePrimitive):
            return self == other or self > other

        return NotImplemented

    # ------------------------------ #

    def __hash__(self) -> int:
        """Computes hash based on `sort_key`

        """
        return hash(self.sort_key)

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

        if self.is_approximate:
            extras.append('≈')

        if self.is_uncertain:
            extras.append('?')

        if self.is_interval:
            extras.append('interval')

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

    value: str = Field(default='')
    language: Optional[str] = Field(default=None)

    # ------------------------------ #

    @classmethod
    @field_validator("language")
    def validate_language_tag(cls, value: Optional[str]) -> Optional[str]:
        """Validation method for 'language' field;

        Checks if the 'language' field matches the BCP format;

        """
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z]{2,3}(-[a-zA-Z0-9]{2,8})*$", value):
            raise ValueError(f"Invalid BCP 47 language tag: '{value}'")

        return value

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
    _geometry: Optional[Any] = PrivateAttr(default=None)

    # ------------------------------ #

    @classmethod
    @field_validator("value")
    def validate_spatial_value(cls, value: str) -> str:
        """Validate that the value is well-formed WKT or GeoJSON;

        If this validator passes, model_post_init is guaranteed to receive a parseable string. Empty strings
        are allowed (unfilled primitive);

        Raises:
            ValueError: If the value is neither valid WKT nor valid GeoJSON;
        
        """
        if not value or not value.strip():
            return value

        value_stripped = value.strip()

        if _WKT_PREFIX.match(value_stripped):
            try:
                from_wkt(value_stripped)
                return value
            except (ValueError, TypeError) as e:
                raise ValueError(
                    f"Invalid WKT: {e}. "
                    f"Input: {value_stripped[:80]}..."
                ) from e

        if value_stripped.startswith("{"):
            try:
                parsed = json.loads(value_stripped)
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"Invalid JSON in spatial value: {e}"
                ) from e
            try:
                shape(parsed)
                return value
            except (AttributeError, KeyError, TypeError) as e:
                raise ValueError(
                    f"Invalid GeoJSON geometry: {e}. "
                    f"Expected a dict with 'type' and 'coordinates'."
                ) from e

        raise ValueError(
            f"Spatial value must be WKT or GeoJSON. "
            f"Got: {value_stripped[:80]}..."
        )

    # ------------------------------ #

    def model_post_init(self, context: Any) -> None:
        """Parse validated value into a pygeoif geometry object;

        Raises:
            RuntimeError: If a validated value cannot be parsed

        """
        if not self.value or not self.value.strip():
            return

        value = self.value.strip()

        if _WKT_PREFIX.match(value):
            self._geometry = from_wkt(value)
        elif value.startswith("{"):
            self._geometry = shape(json.loads(value))
        else:
            raise RuntimeError(
                f"Value passed validation but matches neither "
                f"WKT nor GeoJSON pattern: {value[:80]!r}"
            )

    # ------------------------------ #

    def __repr__(self) -> str:
        return f'{self.value}'


# ******************************************************************************************************************* #


@entity_register(label='E95 SpaceTime Primitive')
class E95SpaceTimePrimitive(E59PrimitiveValue):
    """'E95 SpaceTime Primitive' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E95

    Attributes:
        spatial (E94SpacePrimitive): spatial component (E94SpacePrimitive entity model);
        temporal (E61TimePrimitive): temporl component (E61TimePrimitive entity model);

    """

    spatial: Optional[E94SpacePrimitive] = Field(default=None, description='Spatial component')
    temporal: Optional[E61TimePrimitive] = Field(default=None, description='Temporal component')

    # ------------------------------ #

    @property
    def has_spatial(self) -> bool:
        """Is the spatial component defined;"""
        return self.spatial is not None and bool(self.spatial.value)

    # ------------------------------ #

    @property
    def has_temporal(self) -> bool:
        """Is the temporal component defined."""
        return self.temporal is not None and bool(self.temporal.value)

    # ------------------------------ #

    def __repr__(self) -> str:
        parts = []

        if self.has_spatial:
            parts.append(repr(self.spatial))

        if self.has_temporal:
            parts.append(repr(self.temporal))

        return f"E95({', '.join(parts) or 'empty'})"


# ******************************************************************************************************************* #

# ----------------------------------------------------------------------------------- #
# ----- Coercion functions;                                                     ----- #
# ----- automatically wrap bare Python values in the appropriate CRM primitives ----- #
# ----------------------------------------------------------------------------------- #


def _coerce_e60(value: Any) -> E60Number:
    """Coerce a value to class 'E60Number';

    This function is not intended to be called directly - it is bound to the 'CoercedNumber' type alias;
    Allows users to pass plain numeric values where 'E60Number' is expected;

    Returns:
        E60Number instance;

    Raises:
        ValueError: if value cannot be coerced to E60Number;

    """
    if isinstance(value, E60Number):
        return value

    if isinstance(value, (int, float)):
        return E60Number(value=value)

    if isinstance(value, dict):
        return E60Number(**value)

    raise ValueError(f"Cannot coerce {value!r} to E60")


def _coerce_e61(value: Any) -> E61TimePrimitive:
    """Coerce a value to class 'E61TimePrimitive';

    This function is not intended to be called directly - it is bound to the 'CoercedTime' type alias;
    Allows users to pass plain EDTF strings where 'E61TimePrimitive' is expected;

    Returns:
        E61TimePrimitive instance;

    Raises:
        ValueError: if value cannot be coerced to E61TimePrimitive;

    """
    if isinstance(value, E61TimePrimitive):
        return value

    if isinstance(value, str):
        return E61TimePrimitive(value=value)

    if isinstance(value, dict):
        return E61TimePrimitive(**value)

    raise ValueError(f"Cannot coerce {value!r} to E61")


def _coerce_e62(value: Any) -> E62String:
    """Coerce a value to class 'E62String';

    This function is not intended to be called directly - it is bound to the 'CoercedString' type alias;
    Allows users to pass plain Python strings where 'E62String' is expected;

    Returns:
        E62String instance;

    Raises:
        ValueError: if value cannot be coerced to E62String;

    """
    if isinstance(value, E62String):
        return value

    if isinstance(value, str):
        return E62String(value=value)

    if isinstance(value, dict):
        return E62String(**value)

    raise ValueError(f"Cannot coerce {value!r} to E62")


def _coerce_e94(value: Any) -> E94SpacePrimitive:
    """Coerce a value to class 'E94SpacePrimitive';

    This function is not intended to be called directly - it is bound to the `CoercedSpace` type alias;
    Allows users to pass plain WKT or GeoJSON strings where 'E94SpacePrimitive' is expected;

    Returns:
        E94SpacePrimitive instance;

    Raises:
        ValueError: if value cannot be coerced to E94SpacePrimitive;

    """
    if isinstance(value, E94SpacePrimitive):
        return value

    if isinstance(value, str):
        return E94SpacePrimitive(value=value)

    if isinstance(value, dict):
        return E94SpacePrimitive(**value)

    raise ValueError(f"Cannot coerce {value!r} to E94")


CoercedNumber = Annotated[E60Number, BeforeValidator(_coerce_e60)]
CoercedTime = Annotated[E61TimePrimitive, BeforeValidator(_coerce_e61)]
CoercedString = Annotated[E62String, BeforeValidator(_coerce_e62)]
CoercedSpace = Annotated[E94SpacePrimitive, BeforeValidator(_coerce_e94)]
