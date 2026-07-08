# -*- coding: utf-8 -*-

"""Tests for CRM factory and version loading;

"""

# pylint: disable=E0401,C0116,W0612


import pytest

from pyheritage.cidoc import CRM

# from pyheritage.cidoc.base import ENTITY_REGISTRY
from pyheritage.cidoc.versions import (  # ExtensionNotAvailable,
    VersionNotImplemented,
    VersionNotSupported,
)


class TestCRMFactoryCore:
    """CRM factory — core version resolution;"""

    def test_default_version_is_7_0(self) -> None:
        crm = CRM()
        assert crm.__version__ == "7.0"

    # ------------------------- #

    def test_explicit_version_7_0(self) -> None:
        crm = CRM(version="7.0")
        assert crm.__version__ == "7.0"

    # ------------------------- #

    def test_not_implemented_712_raises(self) -> None:
        with pytest.raises(VersionNotImplemented):
            CRM(version="7.1.2")

    # ------------------------- #

    def test_not_implemented_713_raises(self) -> None:
        with pytest.raises(VersionNotImplemented):
            CRM(version="7.1.3")

    # ------------------------- #

    def test_unsupported_version_raises(self) -> None:
        with pytest.raises(VersionNotSupported):
            CRM(version="9.9.9")

    # ------------------------- #

    def test_unsupported_version_message(self) -> None:
        with pytest.raises(VersionNotSupported, match="9.9.9"):
            CRM(version="9.9.9")

    # ------------------------- #

    def test_not_implemented_version_message(self) -> None:
        with pytest.raises(VersionNotImplemented, match="7.1.2"):
            CRM(version="7.1.2")

    # ------------------------- #

    def test_entities_module_access(self) -> None:
        crm = CRM()
        assert crm.entities is not None

    # ------------------------- #

    def test_properties_module_access(self) -> None:
        crm = CRM()
        assert crm.properties is not None

    # ------------------------- #

    def test_entity_class_accessible_via_module(self) -> None:
        crm = CRM()
        e1 = crm.entities.E1CRMEntity

        assert e1.crm_code == "E1"
        assert e1.crm_label == "E1 CRM Entity"

    # ------------------------- #

    def test_entity_class_accessible_directly(self) -> None:
        crm = CRM()
        e1 = crm.E1CRMEntity
        assert e1.crm_code == "E1"

    # ------------------------- #

    def test_property_class_accessible_via_module(self) -> None:
        crm = CRM()
        P1 = crm.properties.P1IsIdentifiedBy
        assert P1.__name__ == "P1IsIdentifiedBy"

    # ------------------------- #

    def test_invalid_entity_name_raises(self) -> None:
        crm = CRM()
        with pytest.raises(AttributeError):
            crm.NonExistentEntity

    # ------------------------- #

    def test_entity_instantiation_via_factory(self) -> None:
        crm = CRM(version="7.0")
        e1 = crm.E1CRMEntity()
        assert e1.id is not None

    # ------------------------- #

    def test_entity_has_crm_version_attribute(self) -> None:
        crm = CRM()
        assert hasattr(crm.E1CRMEntity, "crm_version")
