# -*- coding: utf-8 -*-

"""CIDOC-CRM v7.0 version package;

Re-exports core CIDOC-CRM 7.0 entities and properties;

"""


from pyheritage.cidoc.versions.v70 import _entities, _properties


__all__ = (
    'entities',
    'properties',
)

# Module-level access to subpackages;
entities = _entities
properties = _properties


# Namespace for model_rebuild — inherited by child versions;
# Contains all v7.0 entity classes + builtins (List, Optional);
__namespace__: dict[str, object] = dict(_entities.__namespace__)
