# -*- coding: utf-8 -*-

"""CIDOC-CRM entity classes;

Represents CIDOC-CRM version 7.0 (released on June 2020);

Models should not be imported directly from this module!;

https://cidoc-crm.org/html/cidoc_crm_v7.0.html

-------------------------
Entities
-------------------------
E59 Primitive Value
E60 Number
E61 Time Primitive
E62 String
E94 Space Primitive
E95 Space-Time Primitive

"""


from __future__ import annotations  # noqa

import json
import math
import re
from typing import Annotated, Any, Optional, Self

from edtf import EDTFObject, parse_edtf, text_to_edtf
from edtf.parser.edtf_exceptions import EDTFParseException
from pydantic import BeforeValidator, Field, field_validator, PrivateAttr
from pygeoif import from_wkt, geometry, shape

from pyheritage.cidoc.core.base import entity_register
from pyheritage.cidoc.core.entities._crm_base import E1CRMEntity
from pyheritage.cidoc.core.enums import SpatialFormat, TimePrecision


__all__ = ('E59PrimitiveValue', 'E60Number', 'E61TimePrimitive', 'E62String', 'E94SpacePrimitive',
           'E95SpaceTimePrimitive', 'CoercedNumber', 'CoercedTime', 'CoercedString', 'CoercedSpace', )


_WKT_PREFIX = re.compile(
    r"^\s*(POINT|LINESTRING|POLYGON|MULTIPOINT|MULTILINESTRING|"
    r"MULTIPOLYGON|GEOMETRYCOLLECTION)\s*[\(Z]",
    re.IGNORECASE,
)

_WKT_TYPES = re.compile(
    r"^\s*(POINT|LINESTRING|POLYGON|MULTIPOINT|MULTILINESTRING|"
    r"MULTIPOLYGON|GEOMETRYCOLLECTION)\s*\(",
    re.IGNORECASE,
)


# ******************************************************************************************************************* #


@entity_register(label='E59 Primitive Value')
class E59PrimitiveValue(E1CRMEntity):
    """'E59 Primitive Value' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E59

    SubClass Of:
        E1 CRM Entity
    SuperClass Of:
        E60 Number
        E61 Time Primitive
        E62 String
        E94 Space Primitive
        E95 Spacetime Primitive
    Scope Note:
        This class comprises values of primitive data types of programming languages or database management systems
        and data types composed of such values used as documentation elements, as well as their mathematical
        abstractions;

        They are not considered as elements of the universe of discourse this model aims at defining and analysing.
        Rather, they play the role of a symbolic interface between the scope of this model and the world of
        mathematical and computational manipulations and the symbolic objects they define and handle;

        In particular they comprise lexical forms encoded as "strings" or series of characters and symbols based
        on encoding schemes (characterised by being a limited subset of the respective mathematical abstractions)
        such as UNICODE and values of datatypes that can be encoded in a lexical form, including quantitative
        specifications of time-spans and geometry. They have in common that instances of E59 Primitive Value define
        themselves by virtue of their encoded value, regardless the nature of their mathematical abstractions;

        Therefore they must not be represented in an implementation by a universal identifier associated with
        a content model of different identity. In a concrete application, it is recommended that the primitive
        value system from a chosen implementation platform and/or data definition language be used to substitute
        for this class and its subclasses;

    Examples:
        - ABCDEFG (E62)
        - 3.14 (E60)
        - 0
        - 1921-01-01 (E61)
    In First Order Logic:
        E59(x) ⊃ E1(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='E60 Number')
class E60Number(E59PrimitiveValue):
    """'E60 Number' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E60

    SubClass Of:
        E59 Primitive Value
    SuperClass Of:
        -
    Scope Note:
        This class comprises any encoding of computable (algebraic) values such as integers, real numbers, complex
        numbers, vectors, tensors etc., including intervals of these values to express limited precision;

        Numbers are fundamentally distinct from numerically expressed identifiers in continua, which are instances of
        E41 Appellation, such as Gregorian dates or spatial coordinates, even though their encoding may be similar.
        Instances of E60 Number can be combined with each other in algebraic operations to yield other instances of
        E60 Number, e.g., 1+1=2. Identifiers in continua may be combined with numbers expressing distances to yield
        new identifiers, e.g., 1924-01-31 + 2 days = 1924-02-02. Cf. E54 Dimension;

    Examples:
        - 5
        - 3+2i
        - 1.5e-04
        - (0.5, - 0.7,88)
    In First Order Logic:
        E60(x) ⊃ E59(x)
    Properties:
        -

    """

    value: int | float = Field(default=0)

    # ------------------------------ #

    @classmethod
    @field_validator("value")
    def must_be_finite(cls, value: float | int) -> float | int:
        """Validation method for 'value' field;"""
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError(f"E60 Number must be finite, got {value}")

        return value

    # ------------------------------ #

    def __int__(self) -> int:
        """Converts value to integer type;"""
        return int(self.value)

    # ------------------------------ #

    def __float__(self) -> float:
        """Converts value to float type;"""
        return float(self.value)

    # ------------------------------ #

    def __repr__(self) -> str:
        return f'E60({self.value})'


# ******************************************************************************************************************* #


@entity_register(label='E61 Time Primitive')
class E61TimePrimitive(E59PrimitiveValue):
    """'E61 Primitive Value' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E61

    SubClass Of:
        E41 Appellation
        E59 Primitive Value
    SuperClass Of:
        -
    Scope Note:
        This class comprises instances of E59 Primitive Value for time that should be implemented with appropriate
        validation, precision and references to temporal coordinate systems to express time in some context relevant
        to cultural and scientific documentation;

        Instantiating different instances of E61 Time Primitive relative to the same instance of E52 Time Span allows
        for the expression of multiple opinions/approximations of the same phenomenon. When representing different
        opinions/approximations of the E52 Time Span of some E2 Temporal Entity, multiple instances of
        E61 Time Primitive should be instantiated relative to one E52 Time Span. Only one E52 Time Span should be
        instantiated since there is only one real phenomenal time extent of any given temporal entity;

        The instances of E61 Time Primitive are not considered as elements of the universe of discourse that the
        CIDOC CRM aims at defining and analysing. Rather, they play the role of a symbolic interface between the
        scope of this model and the world of mathematical and computational manipulations and the symbolic objects
        they define and handle;

        Therefore they must not be represented in an implementation by a universal identifier associated with
        a content model of different identity. In a concrete application, it is recommended that the primitive
        value system from a chosen implementation platform and/or data definition language be used to substitute
        for this class;

    Examples:
        1994 – 1997
        13 May 1768
        2000/01/01 00:00:59.7
        85th century BC
    In First Order Logic:
        E61(x) ⊃ E41(x)
        E61(x) ⊃ E59(x)
    Properties:
        P170 defines time (time is defined by): E52 Time-Span

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
        except EDTFParseException as e:
            raise ValueError(
                f"Invalid EDTF value: '{value}'"
                f"See https://www.loc.gov/standards/datetime/"
            ) from e
        return value

    # ------------------------------ #

    def model_post_init(self, context: Any) -> None:  # noqa
        """Model post init method;

        """
        if self.value:
            try:
                object.__setattr__(self, '_parsed', parse_edtf(self.value.upper()))
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

        if isinstance(other, str):
            other = E61TimePrimitive(value=other)
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

        if isinstance(other, str):
            other = E61TimePrimitive(value=other)
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

        if isinstance(other, str):
            other = E61TimePrimitive(value=other)
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

        if isinstance(other, str):
            other = E61TimePrimitive(value=other)
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

        if isinstance(other, str):
            other = E61TimePrimitive(value=other)
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

    SubClass Of:
        E59 Primitive Value
    SuperClass Of:
        -
    Scope Note:
        This class comprises coherent sequences of binary-encoded symbols. They correspond to the content of an
        instance of E90 Symbolic object. Instances of E62 String represent only the symbol sequence itself. They
        may or may not contain a language code;

        In contrast, instances of other subclasses of E59 Primitive value represent entities in mathematical spaces
        other than that of symbol sequences, by using binary-encoded symbols, such as date expressions or numbers
        in decimal encoding. For instance, different syntactic forms of a date expression may represent the same date
        but consist of different strings;

    Examples:
        - the Quick Brown Fox Jumps Over the Lazy Dog
        - 6F 6E 54 79 70 31 0D 9E
    In First Order Logic:
        E62(x) ⊃ E59(x)
    Properties:
        -

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

    SubClass Of:
        E41 Appellation
        E59 Primitive Value
    SuperClass Of:
        -
    Scope Note:
        This class comprises instances of E59 Primitive Value for space that should be implemented with appropriate
        validation, precision and references to spatial coordinate systems to express geometries on or relative to
        Earth, or on any other stable constellations of matter, relevant to cultural and scientific documentation;

        An instance of E94 Space Primitive defines an instance of E53 Place in the sense of a declarative place as
        elaborated in CRMgeo (Doerr and Hiebel 2013), which means that the identity of the place is derived from its
        geometric definition. Such a declarative place may allow for the approximation of instances of E53 Place
        defined by the actual extent of some phenomenon, such as a settlement or a riverbed, or other forms of
        identification rather than by an instance of E94 Space Primitive. Note that using an instance of
        E94 Space Primitive for approximating the actual extent of some place always defines a (declarative) instance
        of E53 Place in its own right;

        Definitions of instances of E53 Place using different spatial reference systems are always definitions of
        different instances of E53 Place;

        Instances of E94 Space Primitive provide the ability to link CIDOC CRM encoded data to the kinds of geometries
        used in maps or Geoinformation systems. They may be used for visualization of the instances of E53 Place they
        define, in their geographic context and for computing topological relations between places based on these
        geometries. E94 Space Primitive is not further elaborated upon within this model. It is considered good
        practice to maintain compatibility with OGC standards;

    Examples:
        - Coordinate Information in GML like <gml:Point gml:id="p21"
          srsName="http://www.opengis.net/def/crs/EPSG/0/4326"> <gml:coordinates>45.67, 88.56</gml:coordinates>
          </gml:Point>
        - Coordinate Information in lat, long 48,2 13,3
        - Well Known Text like POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
    In First Order Logic:
        E94(x) ⊃ E41(x)
        E94(x) ⊃ E59(x)
    Properties:
        -

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
            f"Spatial value must be WKT or GeoJSON"
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

    @property
    def geometry(self) -> Optional[Any]:
        """Parsed pygeoif geometry object;

        Always available for values that passed validation. None only for empty primitives;

        Returns:
            pygeoif geometry instance or None;

        """
        return self._geometry

    # ------------------------------ #

    @property
    def is_point(self) -> bool:
        """Whether the geometry is a point;"""
        return isinstance(self._geometry, geometry.Point)

    # ------------------------------ #

    @property
    def is_polygon(self) -> bool:
        """Whether the geometry is a polygon or multipolygon;"""
        return isinstance(self._geometry, (geometry.Polygon, geometry.MultiPolygon))

    # ------------------------------ #

    @property
    def is_line(self) -> bool:
        """Whether the geometry is a line or multiline;"""
        return isinstance(self._geometry, (geometry.LineString, geometry.MultiLineString))

    # ------------------------------ #

    @property
    def is_empty(self) -> bool:
        """Whether geometry is empty;"""
        if self._geometry is None:
            return True

        return not (bool(self.value and self.value.strip()))

    # ------------------------------ #

    @property
    def format(self) -> SpatialFormat:
        """Defines spatial format: 'WKT', 'GeopJSON' or 'Unknown';

        """
        if not self.value:
            return SpatialFormat.UNKNOWN

        value = self.value.strip()

        if _WKT_TYPES.match(value):
            return SpatialFormat.WKT

        if value.startswith("{"):
            return SpatialFormat.GEOJSON

        return SpatialFormat.UNKNOWN

    # ------------------------------ #

    @property
    def geometry_type(self) -> Optional[str]:
        """Type of geometry: Point, LineString, Polygon, etc;

        Uses pygeoif geom_type attribute;

        Returns:
            Geometry type string, or None;

        """
        if self._geometry:
            return self._geometry.geom_type

        return None

    # ------------------------------ #

    @property
    def coordinates(self) -> Optional[tuple[float, ...]]:
        """Coordinates for point geometry;

        Returns:
            (longitude, latitude[, altitude]) or None for non-point geometries;

        """
        if isinstance(self._geometry, geometry.Point):
            return tuple(self._geometry.coords[0])

        return None

    # ------------------------------ #

    @property
    def longitude(self) -> Optional[float]:
        """Longitude for a Point geometry;"""
        coordinates = self.coordinates

        return coordinates[0] if coordinates else None

    # ------------------------------ #

    @property
    def latitude(self) -> Optional[float]:
        """Latitude for a Point geometry;"""
        coordinates = self.coordinates

        return coordinates[1] if coordinates else None

    # ------------------------------ #

    @property
    def altitude(self) -> Optional[float]:
        """Altitude for a Point geometry (if altitude is set);"""
        coordinates = self.coordinates

        return coordinates[1] if coordinates else None

    # ------------------------------ #

    @property
    def bounds(self) -> Optional[tuple[float, float, float, float]]:
        """Bounding box: (min_x, min_y, max_x, max_y);

        Returns:
            Bounding box tuple or None;

        """
        if self._geometry:
            return self._geometry.bounds

        return None

    # ------------------------------ #

    @classmethod
    def from_lat_lon(cls, latitude: float, longitude: float, altitude: float = None,
                     srs: str = "EPSG:4326") -> E94SpacePrimitive:
        """Factory method - creates E94 Space Primitive from lat/lon;

        Args:
            latitude (float): point latitude;
            longitude (float): point longitude;
            altitude (float): point altitude (optional);
            srs (str): EPSG code for spatial reference system;

        Returns:
            E94SpacePrimitive object;

        """
        value = f"POINT({longitude} {latitude})" if not altitude else f"POINT({longitude} {latitude} {altitude})"

        return cls(value=value, srs=srs)

    # ------------------------------ #

    @classmethod
    def from_bbox(cls, min_lon: float, min_lat: float, max_lon: float, max_lat: float,
                  srs: str = "EPSG:4326") -> E94SpacePrimitive:
        """Factory method - creates E94 Space Primitive from bounding box;

        Args:
            min_lon (float): minimal bounding box longitude;
            min_lat (float): minimal bounding box latitude;
            max_lon (float): maximal bounding box longitude;
            max_lat (float): maximal bounding box latitude;
            srs (str): EPSG code for spatial reference system;

        Returns:
            E94SpacePrimitive object;

        """
        wkt = (f"POLYGON(({min_lon} {min_lat}, {max_lon} {min_lat}, "
               f"{max_lon} {max_lat}, {min_lon} {max_lat}, "
               f"{min_lon} {min_lat}))")

        return cls(value=wkt, srs=srs)

    # ------------------------------ #

    @classmethod
    def from_geojson(cls, geojson: dict, srs: str = "EPSG:4326") -> E94SpacePrimitive:
        """Factory method - creates E94 Space Primitive entity from GeoJSON;

        Args:
            geojson (dict): GeoJSON;
            srs (str): EPSG code for spatial reference system;

        Returns:
            E94SpacePrimitive object;

        """
        return cls(value=json.dumps(geojson, ensure_ascii=False), srs=srs)

    # ------------------------------ #

    @classmethod
    def from_polygon(cls,
                     exterior: list[tuple[float, float]],
                     holes: Optional[list[list[tuple[float, float]]]] = None,
                     srs: str = "EPSG:4326") -> E94SpacePrimitive:
        """Creates E94 Space Primitive from polygon (list of coordinates);

        Args:
            exterior (list): the outer ring [(lon, lat), ...]; must be closed (first point = last point);
            holes (list): internal rings (holes), (optional);
            srs (str): EPSG code for spatial reference system;

        Examples:
            E94_Space_Primitive.from_polygon([
                (30.4, 31.3), (30.5, 31.3),
                (30.5, 31.4), (30.4, 31.4),
                (30.4, 31.3),
            ])

        """
        polygon = geometry.Polygon(exterior, holes or [])

        return cls(value=polygon.wkt, srs=srs)

    # ------------------------------ #

    @classmethod
    def from_linestring(cls, coordinates: list[tuple[float, float]], srs: str = "EPSG:4326") -> E94SpacePrimitive:
        """Creates E94 Space Primitive from linestring;

        Args:
            coordinates: [(lon, lat), ...] — must contain at least 2 points;
            srs (str): EPSG code for spatial reference system;

        Examples:
            # Mona Lisa way: Florence -> Амбуаз -> Paris
            E94SpacePrimitive.from_linestring([
                (11.26, 43.77),  # Florence
                (0.98, 47.41),   # Amboise
                (2.34, 48.86),   # Paris
            ])

        Returns:
            E94SpacePrimitive object;

        """
        line = geometry.LineString(coordinates)

        return cls(value=line.wkt, srs=srs)

    # ------------------------------ #

    @classmethod
    def from_geometry(cls, geom: geometry, srs: str = "EPSG:4326") -> E94SpacePrimitive:
        """Creates E94 Space Primitive from pygeoif object (or Shapely via __geo_interface__);

        Args:
            geom: any object with .wkt attribute or implementing __geo_interface__;
            srs (str): EPSG code for spatial reference system;

        Returns:
            E94SpacePrimitive object;

        """
        return cls(value=geom.wkt, srs=srs)

    # ------------------------------ #

    def to_wkt(self) -> Optional[str]:
        """Represent as WKT string;

        Works for any geometry type;

        Returns:
            WKT string, or None if geometry is empty;

        """
        if self._geometry:
            return self._geometry.wkt

        return None

    # ------------------------------ #

    def to_geojson(self) -> Optional[dict]:
        """Represent as GeoJSON geometry dict;

        Uses the __geo_interface__ protocol;

        Returns:
            GeoJSON geometry dict, or None;

        """
        if self._geometry:
            return self._geometry.__geo_interface__
        return None

    # ------------------------------ #

    def __repr__(self) -> str:
        return f'{self.value}'


# ******************************************************************************************************************* #


@entity_register(label='E95 SpaceTime Primitive')
class E95SpaceTimePrimitive(E59PrimitiveValue):
    """'E95 SpaceTime Primitive' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E95

    SubClass Of:
        E41 Appellation
        E59 Primitive Value
    SuperClass Of:
        -
    Scope Note:
        This class comprises instances of E59 Primitive Value for spacetime volumes that should be implemented with
        appropriate validation, precision and reference systems to express geometries being limited and varying over
        time on or relative to Earth, or any other stable constellations of matter, relevant to cultural and
        scientific documentation. An instance of E95 Spacetime Primitive may consist of one expression including
        temporal and spatial information such as in GML or a different form of expressing spacetime in an integrated
        way such as a formula containing all 4 dimensions;

        An instance of E95 Spacetime Primitive defines an instance of E92 Spacetime Volume in the sense of
        a declarative spacetime volume as defined in CRMgeo (Doerr & Hiebel 2013), which means that the identity of
        the instance of E92 Spacetime Volume is derived from its geometric and temporal definition. This declarative
        spacetime volume allows for the application of all E92 Spacetime Volume properties to relate phenomenal
        spacetime volumes of periods and physical things to propositions about their spatial and temporal extents;

        Instances of E92 Spacetime Volume defined by P169 that use different spatiotemporal referring systems are
        always regarded as different instances of the E92 Spacetime Volume;

        It is possible for a spacetime volume to be defined by phenomena causal to it, such as an expanding and
        declining realm, a settlement structure or a battle, or other forms of identification rather than by an
        instance of E95 Spacetime Primitive. Any spatiotemporal approximation of such a phenomenon by an instance
        of E95 Spacetime Primitive constitutes an instance of E92 Spacetime Volume in its own right;

        E95 Spacetime Primitive is not further elaborated upon within this model. Compatibility with OGC standards
        are recommended;

    Examples:
        - Spatial and temporal information in KML for the maximum extent of the Byzantine Empire
            <Placemark>
                <name> Byzantine Empire </name>
                <styleUrl>#style_1</styleUrl>
                <TimeSpan>
                    <begin>330</begin>
                    <end>1453</end>
                </TimeSpan>
                <Polygon><altitudeMode>clampToGround</altitudeMode><outerBoundaryIs><LinearRing>
                    <coordinates>18.452787460,40.85553626,0 17.2223187,40.589098,........0 17.2223,39.783
                    </coordinates>
                </Polygon>
            </Placemark>
    In First Order Logic:
        E95(x) ⊃ E41(x)
        E95(x) ⊃ E59(x)
    Properties:
        P169 defines spacetime volume (spacetime volume is defined by): E92 Spacetime Volume

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
