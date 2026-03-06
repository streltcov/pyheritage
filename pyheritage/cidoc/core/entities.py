# -*- coding: utf-8 -*-

"""CIDOC CRM entity models classes;

CRM entrypoint - all entities must be imported only from this module;

"""


from typing import Optional

from pyheritage.cidoc.core._crm_base import E1CRMEntity, E2TemporalEntity, E3ConditionState
from pyheritage.cidoc.core._frame import E52TimeeSpan, E53Place, E54Dimension
from pyheritage.cidoc.core._primitives import (
    E59PrimitiveValue,
    E60Number,
    E61TimePrimitive,
    E62String,
    E94SpacePrimitive,
    E95SpaceTimePrimitive,
)


__all__ = ('E1CRMEntity', 'E2TemporalEntity', 'E3ConditionState', 'E59PrimitiveValue', 'E60Number',
           'E61TimePrimitive', 'E62String', 'E94SpacePrimitive', 'E95SpaceTimePrimitive', )


__builtin_namespace__ = {
    'Optional': Optional,
}


__namespace__ = {
    'E1CRMEntity': E1CRMEntity,
    'E2TemporalEntity': E2TemporalEntity,
    'E3ConditionState': E3ConditionState,
    'E52TimeSpan': E52TimeeSpan,
    'E53Place': E53Place,
    'E54Dimension': E54Dimension,
    'E59PrimitiveValue': E59PrimitiveValue,
    'E60Number': E60Number,
    'E61TimePrimitive': E61TimePrimitive,
    'E62String': E62String,
    'E94TimePrimitive': E94SpacePrimitive,
    'E95SpaceTimePrimitive': E95SpaceTimePrimitive,
}


__namespace__.update(__builtin_namespace__)


E1CRMEntity.model_rebuild(_types_namespace=__namespace__)
E2TemporalEntity.model_rebuild(_types_namespace=__namespace__)
E3ConditionState.model_rebuild(_types_namespace=__namespace__)
E52TimeeSpan.model_rebuild(_types_namespace=__namespace__)
E53Place.model_rebuild(_types_namespace=__namespace__)
E54Dimension.model_rebuild(_types_namespace=__namespace__)
E59PrimitiveValue.model_rebuild(_types_namespace=__namespace__)
E60Number.model_rebuild(_types_namespace=__namespace__)
E61TimePrimitive.model_rebuild(_types_namespace=__namespace__)
E62String.model_rebuild(_types_namespace=__namespace__)
E94SpacePrimitive.model_rebuild(_types_namespace=__namespace__)
E95SpaceTimePrimitive.model_rebuild(_types_namespace=__namespace__)
