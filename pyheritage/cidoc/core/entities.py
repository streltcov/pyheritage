# -*- coding: utf-8 -*-

"""CIDOC-CRM entity classes;

Represents CIDOC-CRM version 7.0 (released on June 2020);

CIDOC-CRM classes and properties - https://cidoc-crm.org/html/cidoc_crm_v7.0.html;

"""


from abc import ABC

from pydantic import BaseModel


__all__ = ('E2TemporalEntity',)


class E1CRMEntity(ABC, BaseModel):
    """Basic Entity model class;

    All other CIDOC CRM models should extend this class;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E1

    SubClass of:
        -

    SuperClass of:
        - E2 Temporal Entity;
        - E52 Time-Span;
        - E53 Place;
        - E54 Dimension;
        - E59 PrimitiveValue;
        - E77 Persistent Item;
        - E92 Spacetime Volume;

    Scope Note:
        This class comprises all things in the universe of discourse of the CIDOC Conceptual Reference Model.
        It is an abstract concept providing for three general properties:
        Identification by name or appellation, and in particular by a preferred identifier
        Classification by type, allowing further refinement of the specific subclass an instance belongs to
        Attachment of free text and other unstructured data for the expression of anything not captured by formal
        properties
        All other classes within the CIDOC CRM are directly or indirectly specialisations of E1 CRM Entity;

    Properties:
        - P1 is identified by (identifies): E41 Appellation
        - P2 has type (is type of): E55 Type
        - P3 has note: E62 String
        - P48 has preferred identifier (is preferred identifier of): E42 Identifier
        - P137 exemplifies (is exemplified by): E55 Type

    """


# ******************************************************************************************************************* #


class E2TemporalEntity(E1CRMEntity):
    """E2 Temporal Entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E2

    SubClass Of:
        - E1 CRM Entity

    SuperClass Of:
        - E3 Condition State
        - E4 Period

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
