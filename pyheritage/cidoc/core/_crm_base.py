# -*- coding: utf-8 -*-

"""CIDOC-CRM  basic models;

Represents CIDOC-CRM version 7.0 (released on June 2020);

https://cidoc-crm.org/html/cidoc_crm_v7.0.html

"""


from abc import ABC

from pyheritage.cidoc.core.base import CRMEntityBase
from pyheritage.cidoc.core.properties import P1IsIdentifiedBy, P2HasType, P3HasNote, P4HasTimeSpan, P5ConsistsOf


__all__ = ('E1CRMEntity', 'E2TemporalEntity', 'E3ConditionState', )


class E1CRMEntity(P1IsIdentifiedBy, P2HasType, P3HasNote, CRMEntityBase, ABC):
    """'E1 CRM Entity' model - basic CRM Entity class;

    All other CIDOC CRM models should extend this class;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E1

    SubClass of:
        -

    SuperClass of:
        E2 Temporal Entity;
        E52 Time-Span;
        E53 Place;
        E54 Dimension;
        E59 PrimitiveValue;
        E77 Persistent Item;
        E92 Spacetime Volume;

    Scope Note:
        This class comprises all things in the universe of discourse of the CIDOC Conceptual Reference Model.
        It is an abstract concept providing for three general properties:
        Identification by name or appellation, and in particular by a preferred identifier
        Classification by type, allowing further refinement of the specific subclass an instance belongs to
        Attachment of free text and other unstructured data for the expression of anything not captured by formal
        properties
        All other classes within the CIDOC CRM are directly or indirectly specialisations of E1 CRM Entity;

    Properties:
        P1 is identified by (identifies): E41 Appellation
        P2 has type (is type of): E55 Type
        P3 has note: E62 String
        P48 has preferred identifier (is preferred identifier of): E42 Identifier
        P137 exemplifies (is exemplified by): E55 Type

    """


# ******************************************************************************************************************* #


class E2TemporalEntity(P4HasTimeSpan, E1CRMEntity):
    """'E2 Temporal Entity' entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E2

    SubClass Of:
        E1 CRM Entity

    SuperClass Of:
        E3 Condition State
        E4 Period

    Scope Note:
        This class comprises all phenomena, such as the instances of E4 Periods and E5 Events, which happen over a
        limited extent in time. This extent in time must be contiguous, i.e., without gaps. In case the defining kinds
        of phenomena for an instance of E2 Temporal Entity cease to happen, and occur later again at another time, we
        regard that the former instance of E2 Temporal Entity has ended and a new instance has come into existence. In
        more intuitive terms, the same event cannot happen twice;
        In some contexts, such phenomena are also called perdurants. This class is disjoint from E77 Persistent Item
        and is an abstract class that typically has no direct instances. E2 Temporal Entity is specialized into
        E4 Period, which applies to a particular geographic area (defined with a greater or lesser degree of
        precision), and E3 Condition State, which applies to instances of E18 Physical Thing;

    """


# ******************************************************************************************************************* #


class E3ConditionState(P5ConsistsOf, E2TemporalEntity):
    """'E3 Condition State' entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E3

    SubClass Of:
        E2 Temporal Entity

    SuperClass Of:
        -

    Scope Note:
        This class comprises the states of objects characterised by a certain condition over a time-span.

        An instance of this class describes the prevailing physical condition of any material object or feature during
        a specific instance of E52 Time Span. In general, the time-span for which a certain condition can be asserted
        may be shorter than the real time-span, for which this condition held;

        The nature of that condition can be described using P2 has type. For example, the instance of
        E3 Condition State “condition of the SS Great Britain between 22 September 1846 and 27 August 1847” can be
        characterized as an instance “wrecked” of E55 Type;

    Examples:
        the "reconstructed" state of the “Amber Room” in Tsarskoje Selo from summer 2003 until now (Owen, 2009)
        the "ruined" state of Peterhof Palace near Saint Petersburg from 1944 to 1946 (Maddox, 2015)
        the state of my turkey in the oven at 14:30 on 25 December, 2002 (P2 has type: E55 Type “still not cooked”)
        the topography of the leaves of Sinai Printed Book 3234.2361 on the 10th of July 2007 (described as: of
        type "cockled")

    In First Order Logic:
        E3(x) ⊃ E2(x)

    Properties:
        P5 consists of (forms part of): E3 Condition State

    """
