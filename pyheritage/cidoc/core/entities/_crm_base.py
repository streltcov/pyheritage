# -*- coding: utf-8 -*-

"""CIDOC-CRM basic model;

Represents CIDOC-CRM version 7.0 (released on June 2020);

https://cidoc-crm.org/html/cidoc_crm_v7.0.html

-------------------------
Entities
-------------------------
E1 CRM Entity

"""


from abc import ABC

from pyheritage.cidoc.base import CRMEntityBase, entity_register
from pyheritage.cidoc.core.properties import (
    P1IsIdentifiedBy,
    P2HasType,
    P3HasNote,
    P48HasPreferredIdentifier,
    P137Exemplifies,
)


__all__ = ('E1CRMEntity', )


@entity_register(label='E1 CRM Entity')
class E1CRMEntity(P1IsIdentifiedBy, P2HasType, P3HasNote, P48HasPreferredIdentifier, P137Exemplifies, CRMEntityBase,
                  ABC):
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
