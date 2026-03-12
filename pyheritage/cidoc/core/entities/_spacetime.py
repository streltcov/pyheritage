# -*- coding: utf-8 -*-

"""Spatial-Temporal CRM frame;

-------------------------
Entities
-------------------------
E52 Time-Span
E53 Place
E54 Dimension
E92 Spacetime Volume
E93 Presence

"""


from pyheritage.cidoc.core.base import entity_register
from pyheritage.cidoc.core.entities._crm_base import E1CRMEntity


__all__ = ('E52TimeeSpan', 'E53Place', 'E54Dimension', 'E92SpaceTimeVolume', 'E93Presence', )


@entity_register(label='E92 Spacetime Volume')
class E92SpaceTimeVolume(E1CRMEntity):
    """'E92 Spacetime Volume' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E92

    SubClass Of:
        E1 CRM Entity
    SuperClass Of:
        E4 Period
        E93 Presence
    Scope Note:
        This class comprises 4 dimensional point sets (volumes) in physical spacetime (in contrast to mathematical
        models of it) regardless their true geometric forms. They may derive their identity from being the extent
        of a material phenomenon or from being the interpretation of an expression defining an extent in spacetime.
        Intersections of instances of E92 Spacetime Volume, E53 Place and E52 Timespan are also regarded as instances
        of E92 Spacetime Volume. An instance of E92 Spacetime Volume is either contiguous or composed of a finite
        number of contiguous subsets. Its boundaries may be fuzzy due to the properties of the phenomena it derives
        from or due to the limited precision up to which defining expression can be identified with a real extent
        in spacetime. The duration of existence of an instance of E92 Spacetime Volume is its projection on time;

    Examples:
        - the extent in space and time of the Event of Caesar’s murder
        - where and when the carbon 14 dating of the "Schoeninger Speer II" in 1996 took place
        - the spatio-temporal trajectory of the H.M.S. Victory from its building to its actual location
        - the extent in space and time defined by a polygon approximating the Danube river flood in Austria between
          6th and 9th of August 2002
    In First Order Logic:
        E92(x) ⊃ E1(x)
    Properties:
        P10 falls within (contains): E92 Spacetime Volume
        P132 spatiotemporally overlaps with: E92 Spacetime Volume
        P133 is spatiotemporally separated from: E92 Spacetime Volume
        P160 has temporal projection (is temporal projection of): E52 Time-Span
        P161 has spatial projection (is spatial projection of): E53 Place

    """


# ******************************************************************************************************************* #


@entity_register(label='E93 Presence')
class E93Presence(E92SpaceTimeVolume):
    """'E93 Presence' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E93

    SubClass Of:
        E92 Spacetime Volume
    SuperClass Of:
        -
    Scope Note:
        This class comprises instances of E92 Spacetime Volume, whose temporal extent has been chosen in order to
        determine the spatial extent of a phenomenon over the chosen time-span. Respective phenomena may, for
        instance, be historical events or periods, but can also be the diachronic extent and existence of physical
        things. In other words, instances of this class fix a slice of another instance of E92 Spacetime Volume
        in time;

        The temporal extent of an instance of E93 Presence typically is predetermined by the researcher so as to
        focus the investigation particularly on finding the spatial extent of the phenomenon by testing for its
        characteristic features. There are at least two basic directions such investigations might take. The
        investigation may wish to determine where something was during some time or it may wish to reconstruct the
        total passage of a phenomenon’s spacetime volume through an examination of discrete presences. Observation
        and measurement of features indicating the presence or absence of a phenomenon in some space allows for the
        progressive approximation of spatial extents through argumentation typically based on inclusion, exclusion
        and various overlaps;

    Examples:
        - The Roman Empire on 19 August AD 14
        - Johann Joachim Winkelmann’s whereabouts in December 1775
        - Johann Joachim Winkelmann’s whereabouts from November 19 1755 until April 9 1768
    In First Order Logic:
        E93(x) ⊃ E92(x)
    Properties:
        P164 during (was time-span of): E52 Time-Span
        P166 was a presence of (had presence): E92 Spacetime Volume
        P167 at (was place of): E53 Place
        P195 was a presence of (had presence): E18 Physical Thing
        P197 covered parts of (was partially covered by): E53 Place

    """


# ******************************************************************************************************************* #


@entity_register(label='E52 Time-Span')
class E52TimeeSpan(E1CRMEntity):
    """'P52 Time-Span' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E52

    SubClass Of:
        E1 CRM Entity
    SuperClass Of:
        -
    Scope Note:
        This class comprises abstract temporal extents, in the sense of Galilean physics, having a beginning, an end
        and a duration;

        Instances of E52 Time-Span have no semantic connotations about phenomena happening within the temporal extent
        they represent. They do not convey any meaning other than a positioning on the “time-line” of chronology. The
        actual extent of an instance of E52 Time-Span can be approximated by properties of E52 Time-Span giving inner
        and outer bounds in the form of dates (instances of E61 Time Primitive). Comparing knowledge about time-spans
        is fundamental for chronological reasoning;

        Some instances of E52 Time-Span may be defined as the actual, in principle observable, temporal extent of
        instances of E2 Temporal Entity via the property P4 has time-span (is time-span of): E52 Time-Span. They
        constitute phenomenal time-spans as defined in CRMgeo (Doerr and Hiebel 2013). Since our knowledge of history
        is imperfect and physical phenomena are fuzzy in nature, the extent of phenomenal time-spans can only be
        described in approximation. An extreme case of approximation, might, for example, define an instance of
        E52 Time-Span having unknown beginning, end and duration. It may, nevertheless, be associated with other
        descriptions by which we can infer knowledge about it, such as in relative chronologies;

        Some instances of E52 may be defined precisely as representing a declaration of a temporal extent, as, for
        instance, done in a business contract. They constitute declarative time-spans as defined in CRMgeo (Doerr and
        Hiebel 2013) and can be described via the property E61 Time Primitive P170 defines time
        (time is defined by): E52 Time-Span;

        When used as a common E52 Time-Span for two events, it will nevertheless describe them as being simultaneous,
        even if nothing else is known;

    Examples:
        - 1961
        - From 12-17-1993 to 12-8-1996
        - 14h30 – 16h22 4th July 1945
        - 9.30 am 1.1.1999 to 2.00 pm 1.1.1999
        - duration of the Ming Dynasty (Chan, 2011)
    In First Order Logic:
        E52(x) ⊃ E1(x)
    Properties:
        P79 beginning is qualified by: E62 String
        P80 end is qualified by: E62 String
        P81 ongoing throughout: E61 Time Primitive
        P82 at some time within: E61 Time Primitive
        P86 falls within (contains): E52 Time-Span
        P191 had duration (was duration of): E54 Dimension

    """


# ******************************************************************************************************************* #


@entity_register(label='E53 Place')
class E53Place(E1CRMEntity):
    """'E53 Place' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E53

    SubClass Of:
        E1 CRM Entity
    SuperClass Of:
        -
    Scope Note:
        This class comprises extents in space, in particular on the surface of the earth, in the pure sense of
        physics: independent from temporal phenomena and matter;

        The instances of E53 Place are usually determined by reference to the position of “immobile” objects such as
        buildings, cities, mountains, rivers, or dedicated geodetic marks, but may also be determined by reference
        to mobile objetcts. A Place can be determined by combining a frame of reference and a location with respect
        to this frame;

        It is sometimes argued that instances of E53 Place are best identified by global coordinates or absolute
        reference systems. However, relative references are often more relevant in the context of cultural
        documentation and tend to be more precise. In particular, we are often interested in position in relation
        to large, mobile objects, such as ships. For example, the Place at which Nelson died is known with reference
        to a large mobile object – H.M.S Victory. A resolution of this Place in terms of absolute coordinates would
        require knowledge of the movements of the vessel and the precise time of death, either of which may be
        revised, and the result would lack historical and cultural relevance;

        Any instance of E18 Physical Thing can serve as a frame of reference for an instance of E53 Place. This may
        be documented using the property P157 is at rest relative to (provides reference space for);

    Examples:
        - the extent of the UK in the year 2003
        - the position of the hallmark on the inside of my wedding ring
        - the place referred to in the phrase: “Fish collected at three miles north of the confluence of the Arve and
          the Rhone”
        - here -> <-
    In First Order Logic:
        E53(x) ⊃ E1(x)
    Properties:
        P89 falls within (contains): E53 Place
        P121 overlaps with: E53 Place
        P122 borders with: E53 Place
        P157 is at rest relative to (provides reference space for): E18 Physical Thing
        P168 place is defined by (defines place): E94 Space Primitive
        P171 at some place within: E94 Space Primitive
        P172 contains: E94 Space Primitive

    """


# ******************************************************************************************************************* #


@entity_register(label="E54 Dimension")
class E54Dimension(E1CRMEntity):
    """'E54 Dimension' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E54

    SubClass Of:
        E1 CRM Entity
    SuperClass Of:
        E97 Monetary Amount
    Scope Note:
        This class comprises quantifiable properties that can be measured by some calibrated means and can be
        approximated by values, i.e. points or regions in a mathematical or conceptual space, such as natural or real
        numbers, RGB values etc;

        An instance of E54 Dimension represents the true quantity, independent from its numerical approximation,
        e.g. in inches or in cm. The properties of the class E54 Dimension allow for expressing the numerical
        approximation of the values of instances of E54 Dimension. If the true values belong to a non-discrete
        space, such as spatial distances, it is recommended to record them as approximations by intervals or regions
        of indeterminacy enclosing the assumed true values. For instance, a length of 5 cm may be recorded as
        4.5-5.5 cm, according to the precision of the respective observation. Note, that interoperability of values
        described in different units depends critically on the representation as value regions;

        Numerical approximations in archaic instances of E58 Measurement Unit used in historical records should be
        preserved. Equivalents corresponding to current knowledge should be recorded as additional instances of
        E54 Dimension as appropriate;

    Examples:
        - The 250 metric ton weight of the Luxor Obelisk
        - The 5.17 m height of the statue of David by Michaelangelo
        - The 530.2 carats of the Great Star of Africa diamond
        - The AD1262-1312, 1303-1384 calibrated C14 date for the Shroud of Turin
        - The 33 m diameter of the Stonehenge Sarcen Circle
        - The 755.9 foot length of the sides of the Great Pyramid at Giza
        - Christies’ hammer price for “Vase with Fifteen Sunflowers” (E97) has currency British Pounds (E98)
        - The time span of the Battle of Issos 333 B.C.E. (E52) had duration Battle of Issos duration (E54)
    In First Order Logic:
        E54(x) ⊃ E1(x)
    Properties:
        P90 has value: E60 Number
        P91 has unit (is unit of): E58 Measurement Unit

    """
