# -*- coding: utf-8 -*-

"""CIDOC-CRM v7.0 version package;

Re-exports core CIDOC-CRM 7.0 entities and properties;
Child versions (v712, v713) inherit from this package and override selectively;

"""


from pyheritage.cidoc.versions.v70 import _entities
from pyheritage.cidoc.versions.v70 import _properties


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
