# -*- coding: utf-8 -*-

"""Tests for D13 Digital Information Carrier;

"""

# pylint: disable=E0401,C0116,W0612

from tests.cidoc.crmdig.helpers import make_e22_kwargs

from pyheritage.cidoc.core.entities import E1CRMEntity, E22HumanMadeObject
from pyheritage.cidoc.crmdig.entities import D13DigitalInformationCarrier
from pyheritage.cidoc.crmdig.properties import L19Stores


class TestD13DigitalInformationCarrier:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D13';"""
        assert D13DigitalInformationCarrier.crm_code == 'D13'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D13 Digital Information Carrier';"""
        assert D13DigitalInformationCarrier.crm_label == 'D13 Digital Information Carrier'

    # ------------------------- #

    def test_inherits_from_e22(self) -> None:
        """Verify D13 inherits from E22 Human-Made Object;"""
        assert issubclass(D13DigitalInformationCarrier, E22HumanMadeObject)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify D13 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(D13DigitalInformationCarrier, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_l19(self) -> None:
        """Verify L19 (stores) mixin is in D13 MRO;"""
        assert L19Stores in D13DigitalInformationCarrier.__mro__

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D13 can be instantiated with required kwargs;"""
        obj = D13DigitalInformationCarrier(**make_e22_kwargs())
        assert obj.id is not None
