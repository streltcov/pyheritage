# -*- coding: utf-8 -*-

"""Tests for D9 Data Object;

"""

# pylint: disable=E0401,C0116,W0612

from pyheritage.cidoc.core.entities import E1CRMEntity, E31Document
from pyheritage.cidoc.crmdig.entities import D1DigitalObject, D9DataObject
from pyheritage.cidoc.crmdig.properties import L61ContainsValueSetOf


class TestD9DataObject:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D9';"""
        assert D9DataObject.crm_code == 'D9'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D9 Data Object';"""
        assert D9DataObject.crm_label == 'D9 Data Object'

    # ------------------------- #

    def test_inherits_from_d1(self) -> None:
        """Verify D9 inherits from D1 Digital Object;"""
        assert issubclass(D9DataObject, D1DigitalObject)

    # ------------------------- #

    def test_inherits_from_e31(self) -> None:
        """Verify D9 inherits from E31 Document;"""
        assert issubclass(D9DataObject, E31Document)

    # ------------------------- #

    def test_mro_includes_l61(self) -> None:
        """Verify L61 (contains value set of) mixin is in D9 MRO;"""
        assert L61ContainsValueSetOf in D9DataObject.__mro__

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify D9 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(D9DataObject, E1CRMEntity)

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D9 can be instantiated with auto-generated ID;"""
        obj = D9DataObject()
        assert obj.id is not None
