# -*- coding: utf-8 -*-

"""CIDOC-CRM v7.0 entity models;

Re-exports all entity classes from core (CIDOC-CRM 7.0 base);

"""


from typing import List, Optional

from pyheritage.cidoc.core import entities as _core_entities
from pyheritage.cidoc.core.entities import (  # noqa: F401, F811, E402 — re-export
    CoercedNumber,
    CoercedSpace,
    CoercedString,
    CoercedTime,
    E1CRMEntity,
    E2TemporalEntity,
    E3ConditionState,
    E4Period,
    E5Event,
    E6Destruction,
    E7Activity,
    E8Acquisition,
    E9Move,
    E10TransferOfCustody,
    E11Modification,
    E12Production,
    E13AttributeAssignment,
    E14ConditionAssessment,
    E15IdentifierAssignment,
    E16Measurement,
    E17TypeAssignment,
    E18PhysicalThing,
    E19PhysicalObject,
    E20BiologicalObject,
    E21Person,
    E22HumanMadeObject,
    E24PhysicalHumanMadeObject,
    E25HumanMadeFeature,
    E26PhysicalFeature,
    E27Site,
    E28ConceptualObject,
    E29DesignOrProcedure,
    E30Right,
    E31Document,
    E32AuthorityDocument,
    E33LinguisticObject,
    E34Inscription,
    E35Title,
    E36VisualItem,
    E37Mark,
    E39Actor,
    E41Appellation,
    E42Identifier,
    E52TimeSpan,
    E53Place,
    E54Dimension,
    E55Type,
    E56Language,
    E57Material,
    E58MeasurementUnit,
    E59PrimitiveValue,
    E60Number,
    E61TimePrimitive,
    E62String,
    E63BeginningOfExistence,
    E64EndOfExistence,
    E65Creation,
    E66Formation,
    E67Birth,
    E68Dissolution,
    E69Death,
    E70Thing,
    E71HumanMadeThing,
    E72LegalObject,
    E73InformationObject,
    E74Group,
    E77PersistentItem,
    E78CuratedHolding,
    E79PartAddition,
    E80PartRemoval,
    E81Transformation,
    E83TypeCreation,
    E85Joining,
    E86Leaving,
    E87CurationActivity,
    E89PropositionalObject,
    E90SymbolicObject,
    E92SpaceTimeVolume,
    E93Presence,
    E94SpacePrimitive,
    E95SpaceTimePrimitive,
    E96Purchase,
    E97MonetaryAmount,
    E98Currency,
    E99ProductType,
)


__all__ = _core_entities.__all__  # type: ignore[has-type]


__builtin_namespace__: dict[str, object] = {
    'List': List,
    'Optional': Optional,
}


__namespace__: dict[str, object] = {}

for name, obj in _core_entities.__namespace__.items():
    __namespace__[name] = obj

__namespace__.update(__builtin_namespace__)

# Clean up namespace helpers;
del name, obj
