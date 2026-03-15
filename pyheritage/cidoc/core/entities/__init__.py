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
    E22HumanMadeObject,
    E24PhysicalHumanMadeObject,
    E25HumanMadeFeature,
    E26PhysicalFeature,
    E27Site,
    E41Appellation,
    E42Identifier,
    E77PersistentItem,
    E78CuratedHolding,
    E90SymbolicObject,
    E97MonetaryAmount,
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
from pyheritage.cidoc.core.entities._temporal import E2TemporalEntity, E3ConditionState


__all__ = ('E1CRMEntity', 'E2TemporalEntity', 'E3ConditionState', 'E18PhysicalThing', 'E19PhysicalObject',
           'E20BiologicalObject', 'E22HumanMadeObject', 'E24PhysicalHumanMadeObject', 'E25HumanMadeFeature',
           'E26PhysicalFeature', 'E27Site', 'E41Appellation', 'E42Identifier', 'E52TimeeSpan', 'E53Place',
           'E54Dimension', 'E59PrimitiveValue', 'E60Number', 'E61TimePrimitive', 'E62String', 'E94SpacePrimitive',
           'E95SpaceTimePrimitive', )


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
    'E18PhysicalThing': E18PhysicalThing,
    'E19PhysicalObject': E19PhysicalObject,
    'E20BiologicalObject': E20BiologicalObject,
    'E22HumanMadeObject': E22HumanMadeObject,
    'E24PhysicalHumanMadeObject': E24PhysicalHumanMadeObject,
    'E25HumanMadeFeature': E25HumanMadeFeature,
    'E26PhysicalFeature': E26PhysicalFeature,
    'E27Site': E27Site,
    'E41Appellation': E41Appellation,
    'E42Identifier': E42Identifier,
    'E52TimeSpan': E52TimeeSpan,
    'E53Place': E53Place,
    'E54Dimension': E54Dimension,
    'E59PrimitiveValue': E59PrimitiveValue,
    'E60Number': E60Number,
    'E61TimePrimitive': E61TimePrimitive,
    'E62String': E62String,
    'E77PersistentItem': E77PersistentItem,
    'E78CuratedHolding': E78CuratedHolding,
    'E90SymbolicObject': E90SymbolicObject,
    'E92SpacePrimitive': E92SpaceTimeVolume,
    'E93Presence': E93Presence,
    'E94TimePrimitive': E94SpacePrimitive,
    'E95SpaceTimePrimitive': E95SpaceTimePrimitive,
    'E97MonetaryAmount': E97MonetaryAmount,
}


__namespace__.update(__builtin_namespace__)


E1CRMEntity.model_rebuild(_types_namespace=__namespace__)
E2TemporalEntity.model_rebuild(_types_namespace=__namespace__)
E3ConditionState.model_rebuild(_types_namespace=__namespace__)
E18PhysicalThing.model_rebuild(_types_namespace=__namespace__)
E19PhysicalObject.model_rebuild(_types_namespace=__namespace__)
E20BiologicalObject.model_rebuild(_types_namespace=__namespace__)
E22HumanMadeObject.model_rebuild(_types_namespace=__namespace__)
E24PhysicalHumanMadeObject.model_rebuild(_types_namespace=__namespace__)
E25HumanMadeFeature.model_rebuild(_types_namespace=__namespace__)
E26PhysicalFeature.model_rebuild(_types_namespace=__namespace__)
E27Site.model_rebuild(_types_namespace=__namespace__)
E41Appellation.model_rebuild(_types_namespace=__namespace__)
E42Identifier.model_rebuild(_types_namespace=__namespace__)
E52TimeeSpan.model_rebuild(_types_namespace=__namespace__)
E53Place.model_rebuild(_types_namespace=__namespace__)
E54Dimension.model_rebuild(_types_namespace=__namespace__)
E59PrimitiveValue.model_rebuild(_types_namespace=__namespace__)
E60Number.model_rebuild(_types_namespace=__namespace__)
E61TimePrimitive.model_rebuild(_types_namespace=__namespace__)
E62String.model_rebuild(_types_namespace=__namespace__)
E77PersistentItem.model_rebuild(_types_namespace=__namespace__)
E78CuratedHolding.model_rebuild(_types_namespace=__namespace__)
E90SymbolicObject.model_rebuild(_types_namespace=__namespace__)
E92SpaceTimeVolume.model_rebuild(_types_namespace=__namespace__)
E93Presence.model_rebuild(_types_namespace=__namespace__)
E94SpacePrimitive.model_rebuild(_types_namespace=__namespace__)
E95SpaceTimePrimitive.model_rebuild(_types_namespace=__namespace__)
E97MonetaryAmount.model_rebuild(_types_namespace=__namespace__)
