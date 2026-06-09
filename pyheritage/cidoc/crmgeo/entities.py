# -*- coding: utf-8 -*-

"""CRMgeo entity models;

CRMgeo v1.2 (original 2015)

Entities
--------
SP1  Phenomenal Spacetime Volume
SP2  Phenomenal Place
SP3  Reference Space
SP4  Spatial Coordinate Reference System
SP5  Geometric Place Expression
SP6  Declarative Place
SP7  Declarative Spacetime Volume
SP10 Declarative Time-Span
SP11 Temporal Reference System
SP12 Spacetime Volume Expression
SP13 Phenomenal Time-Span
SP14 Time Expression
SP15 Geometry

"""


from abc import ABC

from pyheritage.cidoc.base import entity_register
from pyheritage.cidoc.core import entities as _core_entities_module
from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E29DesignOrProcedure,
    E52TimeSpan,
    E53Place,
    E89PropositionalObject,
    E92SpaceTimeVolume,
)
from pyheritage.cidoc.crmgeo.properties import (
    Q6IsAtRestRelativeTo,
    Q7Describes,
    Q8IsFixedOn,
    Q9IsExpressedInTermsOf,
    Q10DefinesPlace,
)


__all__ = (
    'SP1PhenomenalSpacetimeVolume',
    'SP2PhenomenalPlace',
    'SP3ReferenceSpace',
    'SP4SpatialCoordinateReferenceSystem',
    'SP5GeometricPlaceExpression',
    'SP6DeclarativePlace',
    'SP7DeclarativeSpacetimeVolume',
    'SP10DeclarativeTimeSpan',
    'SP11TemporalReferenceSystem',
    'SP13PhenomenalTimeSpan',
)


@entity_register(label='SP1 Phenomenal Spacetime Volume')
class SP1PhenomenalSpacetimeVolume(E92SpaceTimeVolume, ABC):
    """'SP1 Phenomenal Spacetime Volume' CRMgeo entity;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#SP1

    SubClass Of:
        E92 Spacetime Volume

    SuperClass Of:
        SP2 Phenomenal Place

    Scope Note:
        This class comprises the 4 dimensional point sets (volumes) which material
        phenomena occupy in Space-Time. An instance of SP1 Phenomenal Spacetime Volume
        represents the true extent of an instance of E4 Period in spacetime or the true
        extent of the trajectory of an instance of E18 Physical Thing during the course
        of its existence, from production to destruction. A fuzziness of the extent lies
        in the very nature of the phenomenon, and not in the shortcomings of observation.
        The temporal projection of an instance of SP1 defines an E52 Time-Span while its
        spatial projection defines an SP2 Phenomenal Place.

    Examples:
        - The Spacetime Volume of the Event of Caesars murdering
        - The Spacetime Volume where and when the carbon 14 dating of the
          "Schoeninger Speer II" in 1996 took place
        - The spatio-temporal trajectory of the H.M.S. Victory from its building
          to its actual location
        - The Spacetime Volume of the temple in Abu Simbel before its removal

    In First Order Logic:
        SP1(x) ⇒ E92(x)

    Properties:
        (none added yet)

    """


# ******************************************************************************************************************* #


@entity_register(label='SP2 Phenomenal Place')
class SP2PhenomenalPlace(E53Place, ABC):
    """'SP2 Phenomenal Place' CRMgeo entity;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#SP2

    SubClass Of:
        E53 Place

    Scope Note:
        This class comprises instances of E53 Place whose extent and position is
        defined by the spatial projection of the spatiotemporal extent of a real world
        phenomenon that can be observed or measured. The spatial projection depends on
        the instance of SP3 Reference Space onto which the extent of the phenomenon is
        projected. In general, there are no limitations to the number of Reference Spaces
        one could regard, but only few choices are relevant for the cultural-historical
        discourse. Typical for the archaeological discourse is to choose a reference space
        with respect to which the remains of some events would stay at the same place,
        for instance, relative to the bedrock of a continental plate.

    Examples:
        - The place where the murder of Caesar happened
        - Place on H.M.S. Victory at which Nelson died
        - The Place of the Varus Battle
        - The volume in space of my wine glass
        - The space enclosed by this room
        - The space in borehole Nr. 405

    In First Order Logic:
        SP2(x) ⇒ E53(x)

    Properties:
        (none added yet)

    """


# ******************************************************************************************************************* #


@entity_register(label='SP3 Reference Space')
class SP3ReferenceSpace(Q6IsAtRestRelativeTo, E1CRMEntity, ABC):
    """'SP3 Reference Space' CRMgeo entity;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#SP3

    SubClass Of:
        E1 CRM Entity

    Scope Note:
        This class comprises the (typically Euclidian) Space that is at rest in
        relation to an instance of E18 Physical Thing and extends infinitely beyond it.
        It is the space in which we typically expect things to stay in place if no
        particular natural or human distortion processes occur. This definition requires
        that at least essential parts of the respective physical thing have a stability
        of form. An instance of SP3 Reference Space begins to exist with the largest
        thing that is at rest in it and ceases to exist with its E6 Destruction. If
        other things are at rest in the same space and their time-span of existence
        falls within the one of the reference object, they share the same reference space.

    Examples:
        - The Space inside and around H.M.S. Victory while it is moving through
          the Atlantic Ocean
        - The Space inside and around the Eurasian Continental Plate
        - The Space inside and around the Earth
        - The Space inside and around the Solar system

    In First Order Logic:
        SP3(x) ⇒ E1(x)

    Properties:
        (none added yet)

    """


# ******************************************************************************************************************* #


@entity_register(label='SP4 Spatial Coordinate Reference System')
class SP4SpatialCoordinateReferenceSystem(Q7Describes, Q8IsFixedOn, E29DesignOrProcedure):
    """'SP4 Spatial Coordinate Reference System' CRMgeo entity;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#SP4

    SubClass Of:
        E29 Design or Procedure

    Scope Note:
        This class comprises systems that are used to describe locations in a SP3
        Reference Space. An instance of SP4 Spatial Coordinate Reference System is
        composed of two parts: The first is a Coordinate System which is a set of
        coordinate axes with specified units of measurement and axis directions. The
        second part is a set of reference features at rest in the Reference Space it
        describes in the real world that relate the Coordinate System to real world
        locations and fix it with respect to the reference object of its Reference
        Space. In surveying and geodesy, such a system is called a datum. SP4 Spatial
        Coordinate Reference Systems have a validity for a certain spatial extent of
        the SP3 Reference Space and in addition a temporal validity.

    Examples:
        - Longitude-Latitude (ellipsoidal Coordinate System) in WGS84 (Datum)
        - EPSG 3241
        - The coordinate system to describe locations on H.M.S. Victory taking the
          deck foundation of the middle mast as origin, the mast as z axis, the line
          at right angle to the bow line as x axis and a right angle to both as y axis
        - The printed lines of the millimeter paper on which an archaeological
          feature is drawn

    In First Order Logic:
        SP4(x) ⇒ E29(x)

    Properties:
        (none added yet)

    """


# ******************************************************************************************************************* #


@entity_register(label='SP5 Geometric Place Expression')
class SP5GeometricPlaceExpression(Q9IsExpressedInTermsOf, Q10DefinesPlace, E1CRMEntity, ABC):
    """'SP5 Geometric Place Expression' CRMgeo entity;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#SP5

    SubClass Of:
        E1 CRM Entity

    SuperClass Of:
        SP15 Geometry

    Scope Note:
        This class comprises the expressions that define the extent and position
        of instances of SP6 Declarative Place in terms of a specific SP4 Spatial
        Coordinate Reference System. It may consist of coordinates or other
        geometric descriptions. Instances of SP5 Geometric Place Expression are
        regarded as immaterial items in the sense of information objects.

    Examples:
        - The GML point representation "45.67 88.56"
        - A polygon approximating the boundaries of the UK

    In First Order Logic:
        SP5(x) ⇒ E1(x)

    Properties:
        Q9 is expressed in terms of: SP4 Spatial Coordinate Reference System
        Q10 defines place: SP6 Declarative Place

    """


# ******************************************************************************************************************* #


@entity_register(label='SP6 Declarative Place')
class SP6DeclarativePlace(E53Place, E89PropositionalObject):
    """'SP6 Declarative Place' CRMgeo entity;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#SP6

    SubClass Of:
        E53 Place
        E89 Propositional Object

    SuperClass Of:
        SP15 Geometry

    Scope Note:
        This class comprises instances of E53 Place whose extent and position is
        defined by a SP5 Geometric Place Expression. There is one implicit or explicit
        SP3 Reference Space in which the SP5 Place Expression describes the intended
        place. Even though SP5 Geometric Place Expressions have an unlimited precision,
        measurement devices and the precision of the position of reference features
        relating the SP4 Spatial Coordinate Reference System to a SP3 Reference Space
        impose limitations to the determination of an SP6 Declarative Place in the real
        world. Several SP5 Geometric Place Expressions may denote the same SP6
        Declarative Place if their precision falls within the same range. Instances of
        SP6 Declarative Places may be used to approximate instances of E53 Places or
        parts of them.

    Examples:
        - The place defined by a GML point with coordinates 45.67, 88.56 in WGS84
        - The place defined by a line approximating the Danube river
        - The place of the Orinoco river defined in the map of Diego Ribeiro in 1529
        - The place defined through a polygon that represents the boundaries of the
          UK in the year 2003

    In First Order Logic:
        SP6(x) ⇒ E53(x)
        SP6(x) ⇒ E89(x)

    Properties:
        (none added yet)

    """


# ******************************************************************************************************************* #


@entity_register(label='SP7 Declarative Spacetime Volume')
class SP7DeclarativeSpacetimeVolume(E92SpaceTimeVolume, E89PropositionalObject):
    """'SP7 Declarative Spacetime Volume' CRMgeo entity;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#SP7

    SubClass Of:
        E92 Spacetime Volume
        E89 Propositional Object

    Scope Note:
        This class comprises instances of E92 Spacetime Volumes whose temporal and
        spatial extent and position is defined by a SP12 Spacetime Volume Expression.
        There is one implicit or explicit SP3 Reference Space in which the SP12
        Spacetime Volume Expression describes the intended Spacetime Volume. As we
        restrict the model to Galilean physics and explicitly exclude systems with
        velocities close to the speed of light we do not model a "Reference Time" as
        it would be necessary for relativistic physics. Even though SP12 Spacetime
        Volume Expressions have an unlimited precision, measurement devices and the
        precision of the position of reference features relating the SP4 Spatial
        Coordinate Reference System to a SP3 Reference Space impose limitations to
        the determination of the spatial part of an SP7 Declarative Spacetime Volume
        in the real world. Several SP12 Spacetime Volume Expressions may denote the
        same SP7 Declarative Spacetime Volume if their precision falls within the
        same range.

    Examples:
        - The spacetime volume defined by a polygon approximating the Danube river
          flood in Austria between 6th and 9th of August 2002
        - The spacetime volume of the Orinoco river in 1529 defined in the map of
          Diego Ribeiro in 1529
        - The spacetime volume representing the boundaries of the UK from 1900-1950

    In First Order Logic:
        SP7(x) ⇒ E92(x)
        SP7(x) ⇒ E89(x)

    Properties:
        (none added yet)

    """


# ******************************************************************************************************************* #


@entity_register(label='SP10 Declarative Time-Span')
class SP10DeclarativeTimeSpan(E52TimeSpan, E89PropositionalObject):
    """'SP10 Declarative Time-Span' CRMgeo entity;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#SP10

    SubClass Of:
        E52 Time-Span
        E89 Propositional Object

    Scope Note:
        This class comprises instances of E52 Time-Spans that represent the Time
        Span defined by a SP14 Time Expression. Thus they derive their identity
        through an expression defining an extent in time. Even though SP10 Declarative
        Time Spans have an unlimited precision, measurement devices and the possible
        precision within the SP11 Temporal Reference System impose limitations to the
        determination of an SP10 Declarative Time Span. The accuracy of an SP10
        Declarative Time Span depends upon the documentation and measurement method.
        SP10 Declarative Time Spans may be used to approximate actual (phenomenal)
        Time-Spans of temporal entities.

    Examples:
        - Extent in time defined by the expression "1961"
        - Extent in time defined by the expression "From 12-17-1993 to 12-8-1996"
        - Extent in time defined by the expression "14h30 - 16h22 4th July 1945"

    In First Order Logic:
        SP10(x) ⇒ E52(x)
        SP10(x) ⇒ E89(x)

    Properties:
        (none added yet)

    """


# ******************************************************************************************************************* #


@entity_register(label='SP11 Temporal Reference System')
class SP11TemporalReferenceSystem(E29DesignOrProcedure):
    """'SP11 Temporal Reference System' CRMgeo entity;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#SP11

    SubClass Of:
        E29 Design or Procedure

    Scope Note:
        This class comprises systems that are used to describe positions and extents
        in a Reference Time. If relativistic effects are negligible in the wider
        spacetime area of interest and the speeds of associated things, then there is
        only one unique global reference time. The typical way to measure time is to
        count the cycles of a periodic process for which we have a hypothesis of
        constant frequency, such as oscillations of a crystal, molecular arrangement,
        rotation of earth around itself or around the sun. The origin for a Temporal
        Reference System is fixed on a reference event. As long as the number of
        cycles passed from that reference event until now are known, the temporal
        reference system exists and expressions in this Reference System can be
        interpreted with respect to the Reference Time.

    Examples:
        - Gregorian Calendar
        - Coordinated Universal Time (UTC)
        - Julian date
        - ISO 8601

    In First Order Logic:
        SP11(x) ⇒ E29(x)

    Properties:
        (none added yet)

    """


# ******************************************************************************************************************* #


@entity_register(label='SP13 Phenomenal Time-Span')
class SP13PhenomenalTimeSpan(E52TimeSpan, ABC):
    """'SP13 Phenomenal Time-Span' CRMgeo entity;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#SP13

    SubClass Of:
        E52 Time-Span

    Scope Note:
        This class comprises instances of E52 Time-Spans whose extent and position is
        defined by the temporal projection of the spatiotemporal extent that can be
        observed or measured. Thus they derive their identity through the extent in
        time of a real world phenomenon.

    Examples:
        - Duration of the phenomenal temporal extent of the Trafalgar battle
        - The real duration of the Ming Dynasty
        - The real extent of the lifetime of Caesar starting with his birth and
          ending with his death

    In First Order Logic:
        SP13(x) ⇒ E52(x)

    Properties:
        (none added yet)

    """


# ******************************************************************************************************************* #


__crmgeo_namespace__ = {
    'SP1PhenomenalSpacetimeVolume': SP1PhenomenalSpacetimeVolume,
    'SP2PhenomenalPlace': SP2PhenomenalPlace,
    'SP3ReferenceSpace': SP3ReferenceSpace,
    'SP4SpatialCoordinateReferenceSystem': SP4SpatialCoordinateReferenceSystem,
    'SP5GeometricPlaceExpression': SP5GeometricPlaceExpression,
    'SP6DeclarativePlace': SP6DeclarativePlace,
    'SP7DeclarativeSpacetimeVolume': SP7DeclarativeSpacetimeVolume,
    'SP10DeclarativeTimeSpan': SP10DeclarativeTimeSpan,
    'SP11TemporalReferenceSystem': SP11TemporalReferenceSystem,
    'SP13PhenomenalTimeSpan': SP13PhenomenalTimeSpan,
}


__namespace__ = {**_core_entities_module.__namespace__, **__crmgeo_namespace__}


SP1PhenomenalSpacetimeVolume.model_rebuild(_types_namespace=__namespace__)
SP2PhenomenalPlace.model_rebuild(_types_namespace=__namespace__)
SP3ReferenceSpace.model_rebuild(_types_namespace=__namespace__)
SP4SpatialCoordinateReferenceSystem.model_rebuild(_types_namespace=__namespace__)
SP5GeometricPlaceExpression.model_rebuild(_types_namespace=__namespace__)
SP6DeclarativePlace.model_rebuild(_types_namespace=__namespace__)
SP7DeclarativeSpacetimeVolume.model_rebuild(_types_namespace=__namespace__)
SP10DeclarativeTimeSpan.model_rebuild(_types_namespace=__namespace__)
SP11TemporalReferenceSystem.model_rebuild(_types_namespace=__namespace__)
SP13PhenomenalTimeSpan.model_rebuild(_types_namespace=__namespace__)
