# -*- coding: utf-8 -*-

"""Tests for D1 Digital Object;

"""

# pylint: disable=E0401,C0116,W0612

from pyheritage.cidoc.core.entities import E1CRMEntity, E73InformationObject
from pyheritage.cidoc.crmdig.entities import D1DigitalObject


class TestD1DigitalObject:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D1';"""
        assert D1DigitalObject.crm_code == 'D1'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D1 Digital Object';"""
        assert D1DigitalObject.crm_label == 'D1 Digital Object'

    # ------------------------- #

    def test_inherits_from_e73(self) -> None:
        """Verify D1 inherits from E73 Information Object;"""
        assert issubclass(D1DigitalObject, E73InformationObject)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify D1 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(D1DigitalObject, E1CRMEntity)

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D1 can be instantiated with auto-generated ID;"""
        obj = D1DigitalObject()
        assert obj.id is not None
