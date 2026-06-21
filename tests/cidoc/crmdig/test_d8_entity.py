# -*- coding: utf-8 -*-

"""Tests for D8 Digital Device;

"""

# pylint: disable=E0401,C0116,W0612

from tests.cidoc.crmdig.helpers import make_e22_kwargs

from pyheritage.cidoc.core.entities import E1CRMEntity, E22HumanMadeObject
from pyheritage.cidoc.crmdig.entities import D8DigitalDevice


class TestD8DigitalDevice:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D8';"""
        assert D8DigitalDevice.crm_code == 'D8'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D8 Digital Device';"""
        assert D8DigitalDevice.crm_label == 'D8 Digital Device'

    # ------------------------- #

    def test_inherits_from_e22(self) -> None:
        """Verify D8 inherits from E22 Human-Made Object;"""
        assert issubclass(D8DigitalDevice, E22HumanMadeObject)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify D8 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(D8DigitalDevice, E1CRMEntity)

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D8 can be instantiated with required kwargs;"""
        obj = D8DigitalDevice(**make_e22_kwargs())
        assert obj.id is not None
