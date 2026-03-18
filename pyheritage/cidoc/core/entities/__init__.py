# -*- coding: utf-8 -*-

"""CIDOC CRM entity models classes;

CRM entrypoint - all entities must be imported only from this module;

"""


from typing import Optional

from pyheritage.cidoc.core.entities._crm_base import E1CRMEntity
from pyheritage.cidoc.core.entities._persistent import (
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
    E55Type,
    E56Language,
    E57Material,
    E58MeasurementUnit,
    E70Thing,
    E71HumanMadeThing,
    E72LegalObject,
    E73InformationObject,
    E74Group,
    E77PersistentItem,
    E78CuratedHolding,
    E89PropositionalObject,
    E90SymbolicObject,
    E97MonetaryAmount,
    E98Currency,
    E99ProductType,
)
from pyheritage.cidoc.core.entities._primitives import (
    CoercedNumber,
    CoercedSpace,
    CoercedString,
    CoercedTime,
    E59PrimitiveValue,
    E60Number,
    E61TimePrimitive,
    E62String,
    E94SpacePrimitive,
    E95SpaceTimePrimitive,
)
from pyheritage.cidoc.core.entities._spacetime import (
    E52TimeeSpan,
    E53Place,
    E54Dimension,
    E92SpaceTimeVolume,
    E93Presence,
)
from pyheritage.cidoc.core.entities._temporal import (
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
    E63BeginningOfExistence,
    E64EndOfExistence,
    E65Creation,
    E66Formation,
    E67Birth,
    E68Dissolution,
    E69Death,
    E79PartAddition,
    E80PartRemoval,
    E81Transformation,
    E83TypeCreation,
    E85Joining,
    E86Leaving,
    E87CurationActivity,
    E96Purchase,
)


__all__ = ('E1CRMEntity', 'E2TemporalEntity', 'E3ConditionState', 'E4Period', 'E5Event', 'E6Destruction',
           'E7Activity', 'E8Acquisition', 'E9Move', 'E10TransferOfCustody', 'E11Modification', 'E12Production',
           'E13AttributeAssignment', 'E14ConditionAssessment', 'E15IdentifierAssignment', 'E16Measurement',
           'E17TypeAssignment', 'E18PhysicalThing', 'E19PhysicalObject', 'E20BiologicalObject', 'E21Person',
           'E22HumanMadeObject', 'E24PhysicalHumanMadeObject', 'E25HumanMadeFeature', 'E26PhysicalFeature', 'E27Site',
           'E28ConceptualObject', 'E29DesignOrProcedure', 'E30Right', 'E31Document', 'E32AuthorityDocument',
           'E33LinguisticObject', 'E34Inscription', 'E35Title', 'E36VisualItem', 'E37Mark', 'E39Actor',
           'E41Appellation', 'E42Identifier', 'E52TimeeSpan', 'E53Place', 'E54Dimension', 'E55Type', 'E56Language',
           'E57Material', 'E58MeasurementUnit', 'E59PrimitiveValue', 'E60Number', 'E61TimePrimitive', 'E62String',
           'E63BeginningOfExistence', 'E64EndOfExistence', 'E65Creation', 'E66Formation', 'E67Birth',
           'E68Dissolution', 'E69Death', 'E70Thing', 'E71HumanMadeThing', 'E72LegalObject', 'E73InformationObject',
           'E74Group', 'E77PersistentItem', 'E78CuratedHolding', 'E79PartAddition', 'E80PartRemoval',
           'E81Transformation', 'E83TypeCreation', 'E85Joining', 'E86Leaving', 'E87CurationActivity',
           'E89PropositionalObject', 'E90SymbolicObject', 'E92SpaceTimeVolume', 'E93Presence', 'E94SpacePrimitive',
           'E95SpaceTimePrimitive', 'E96Purchase', 'E97MonetaryAmount', 'E98Currency', 'E99ProductType', )


__builtin_namespace__ = {
    'Optional': Optional,
}


__namespace__ = {
    'CoercedNumber': CoercedNumber,
    'CoercedSpace': CoercedSpace,
    'CoercedString': CoercedString,
    'CoercedTime': CoercedTime,
    'E1CRMEntity': E1CRMEntity,
    'E2TemporalEntity': E2TemporalEntity,
    'E3ConditionState': E3ConditionState,
    'E4Period': E4Period,
    'E5Event': E5Event,
    'E6Destruction': E6Destruction,
    'E7Activity': E7Activity,
    'E8Acquisition': E8Acquisition,
    'E9Move': E9Move,
    'E10TransferOfCustody': E10TransferOfCustody,
    'E11Modification': E11Modification,
    'E12Production': E12Production,
    'E13AttributeAssignment': E13AttributeAssignment,
    'E14ConditionAssessment': E14ConditionAssessment,
    'E15IdentifierAssignment': E15IdentifierAssignment,
    'E16Measurement': E16Measurement,
    'E17TypeAssignment': E17TypeAssignment,
    'E18PhysicalThing': E18PhysicalThing,
    'E19PhysicalObject': E19PhysicalObject,
    'E20BiologicalObject': E20BiologicalObject,
    'E21Person': E21Person,
    'E22HumanMadeObject': E22HumanMadeObject,
    'E24PhysicalHumanMadeObject': E24PhysicalHumanMadeObject,
    'E25HumanMadeFeature': E25HumanMadeFeature,
    'E26PhysicalFeature': E26PhysicalFeature,
    'E27Site': E27Site,
    'E28ConceptualObject': E28ConceptualObject,
    'E29DesignOrProcedure': E29DesignOrProcedure,
    'E30Right': E30Right,
    'E31Document': E31Document,
    'E32AuthorityDocument': E32AuthorityDocument,
    'E33LinguisticObject': E33LinguisticObject,
    'E34Inscription': E34Inscription,
    'E35Title': E35Title,
    'E36VisualItem': E36VisualItem,
    'E37Mark': E37Mark,
    'E39Actor': E39Actor,
    'E41Appellation': E41Appellation,
    'E42Identifier': E42Identifier,
    'E52TimeSpan': E52TimeeSpan,
    'E53Place': E53Place,
    'E54Dimension': E54Dimension,
    'E55Type': E55Type,
    'E56Language': E56Language,
    'E57Material': E57Material,
    'E58MeasurementUnit': E58MeasurementUnit,
    'E59PrimitiveValue': E59PrimitiveValue,
    'E60Number': E60Number,
    'E61TimePrimitive': E61TimePrimitive,
    'E62String': E62String,
    'E63BeginningOfExistence': E63BeginningOfExistence,
    'E64EndOfExistence': E64EndOfExistence,
    'E65Creation': E65Creation,
    'E66Formation': E66Formation,
    'E67Birth': E67Birth,
    'E68Dissolution': E68Dissolution,
    'E69Death': E69Death,
    'E70Thing': E70Thing,
    'E71HumanMadeThing': E71HumanMadeThing,
    'E72LegalObject': E72LegalObject,
    'E73InformationObject': E73InformationObject,
    'E74Group': E74Group,
    'E77PersistentItem': E77PersistentItem,
    'E78CuratedHolding': E78CuratedHolding,
    'E79PartAddition': E79PartAddition,
    'E80PartRemoval': E80PartRemoval,
    'E81Transformation': E81Transformation,
    'E83TypeCreation': E83TypeCreation,
    'E85Joining': E85Joining,
    'E86Leaving': E86Leaving,
    'E87CurationActivity': E87CurationActivity,
    'E89PropositionalObject': E89PropositionalObject,
    'E90SymbolicObject': E90SymbolicObject,
    'E92SpacePrimitive': E92SpaceTimeVolume,
    'E93Presence': E93Presence,
    'E94TimePrimitive': E94SpacePrimitive,
    'E95SpaceTimePrimitive': E95SpaceTimePrimitive,
    'E96Purchase': E96Purchase,
    'E97MonetaryAmount': E97MonetaryAmount,
    'E98Currency': E98Currency,
    'E99ProductType': E99ProductType,
}


__namespace__.update(__builtin_namespace__)


E1CRMEntity.model_rebuild(_types_namespace=__namespace__)
E2TemporalEntity.model_rebuild(_types_namespace=__namespace__)
E3ConditionState.model_rebuild(_types_namespace=__namespace__)
E4Period.model_rebuild(_types_namespace=__namespace__)
E5Event.model_rebuild(_types_namespace=__namespace__)
E6Destruction.model_rebuild(_types_namespace=__namespace__)
E7Activity.model_rebuild(_types_namespace=__namespace__)
E8Acquisition.model_rebuild(_types_namespace=__namespace__)
E9Move.model_rebuild(_types_namespace=__namespace__)
E10TransferOfCustody.model_rebuild(_types_namespace=__namespace__)
E11Modification.model_rebuild(_types_namespace=__namespace__)
E12Production.model_rebuild(_types_namespace=__namespace__)
E13AttributeAssignment.model_rebuild(_types_namespace=__namespace__)
E14ConditionAssessment.model_rebuild(_types_namespace=__namespace__)
E15IdentifierAssignment.model_rebuild(_types_namespace=__namespace__)
E16Measurement.model_rebuild(_types_namespace=__namespace__)
E17TypeAssignment.model_rebuild(_types_namespace=__namespace__)
E18PhysicalThing.model_rebuild(_types_namespace=__namespace__)
E19PhysicalObject.model_rebuild(_types_namespace=__namespace__)
E20BiologicalObject.model_rebuild(_types_namespace=__namespace__)
E21Person.model_rebuild(_types_namespace=__namespace__)
E22HumanMadeObject.model_rebuild(_types_namespace=__namespace__)
E24PhysicalHumanMadeObject.model_rebuild(_types_namespace=__namespace__)
E25HumanMadeFeature.model_rebuild(_types_namespace=__namespace__)
E26PhysicalFeature.model_rebuild(_types_namespace=__namespace__)
E27Site.model_rebuild(_types_namespace=__namespace__)
E28ConceptualObject.model_rebuild(_types_namespace=__namespace__)
E29DesignOrProcedure.model_rebuild(_types_namespace=__namespace__)
E30Right.model_rebuild(_types_namespace=__namespace__)
E31Document.model_rebuild(_types_namespace=__namespace__)
E32AuthorityDocument.model_rebuild(_types_namespace=__namespace__)
E33LinguisticObject.model_rebuild(_types_namespace=__namespace__)
E34Inscription.model_rebuild(_types_namespace=__namespace__)
E35Title.model_rebuild(_types_namespace=__namespace__)
E36VisualItem.model_rebuild(_types_namespace=__namespace__)
E37Mark.model_rebuild(_types_namespace=__namespace__)
E39Actor.model_rebuild(_types_namespace=__namespace__)
E41Appellation.model_rebuild(_types_namespace=__namespace__)
E42Identifier.model_rebuild(_types_namespace=__namespace__)
E52TimeeSpan.model_rebuild(_types_namespace=__namespace__)
E53Place.model_rebuild(_types_namespace=__namespace__)
E54Dimension.model_rebuild(_types_namespace=__namespace__)
E55Type.model_rebuild(_types_namespace=__namespace__)
E56Language.model_rebuild(_types_namespace=__namespace__)
E57Material.model_rebuild(_types_namespace=__namespace__)
E58MeasurementUnit.model_rebuild(_types_namespace=__namespace__)
E59PrimitiveValue.model_rebuild(_types_namespace=__namespace__)
E60Number.model_rebuild(_types_namespace=__namespace__)
E61TimePrimitive.model_rebuild(_types_namespace=__namespace__)
E62String.model_rebuild(_types_namespace=__namespace__)
E63BeginningOfExistence.model_rebuild(_types_namespace=__namespace__)
E64EndOfExistence.model_rebuild(_types_namespace=__namespace__)
E65Creation.model_rebuild(_types_namespace=__namespace__)
E66Formation.model_rebuild(_types_namespace=__namespace__)
E67Birth.model_rebuild(_types_namespace=__namespace__)
E68Dissolution.model_rebuild(_types_namespace=__namespace__)
E69Death.model_rebuild(_types_namespace=__namespace__)
E70Thing.model_rebuild(_types_namespace=__namespace__)
E71HumanMadeThing.model_rebuild(_types_namespace=__namespace__)
E72LegalObject.model_rebuild(_types_namespace=__namespace__)
E73InformationObject.model_rebuild(_types_namespace=__namespace__)
E74Group.model_rebuild(_types_namespace=__namespace__)
E77PersistentItem.model_rebuild(_types_namespace=__namespace__)
E78CuratedHolding.model_rebuild(_types_namespace=__namespace__)
E79PartAddition.model_rebuild(_types_namespace=__namespace__)
E80PartRemoval.model_rebuild(_types_namespace=__namespace__)
E81Transformation.model_rebuild(_types_namespace=__namespace__)
E83TypeCreation.model_rebuild(_types_namespace=__namespace__)
E85Joining.model_rebuild(_types_namespace=__namespace__)
E86Leaving.model_rebuild(_types_namespace=__namespace__)
E87CurationActivity.model_rebuild(_types_namespace=__namespace__)
E89PropositionalObject.model_rebuild(_types_namespace=__namespace__)
E90SymbolicObject.model_rebuild(_types_namespace=__namespace__)
E92SpaceTimeVolume.model_rebuild(_types_namespace=__namespace__)
E93Presence.model_rebuild(_types_namespace=__namespace__)
E94SpacePrimitive.model_rebuild(_types_namespace=__namespace__)
E95SpaceTimePrimitive.model_rebuild(_types_namespace=__namespace__)
E96Purchase.model_rebuild(_types_namespace=__namespace__)
E97MonetaryAmount.model_rebuild(_types_namespace=__namespace__)
E98Currency.model_rebuild(_types_namespace=__namespace__)
E99ProductType.model_rebuild(_types_namespace=__namespace__)
