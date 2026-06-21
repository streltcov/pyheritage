# -*- coding: utf-8 -*-

"""Tests for D14 Software;

"""

# pylint: disable=E0401,C0116,W0612

from pyheritage.cidoc.core.entities import E1CRMEntity
from pyheritage.cidoc.crmdig.entities import D1DigitalObject, D14Software


class TestD14Software:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D14';"""
        assert D14Software.crm_code == 'D14'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D14 Software';"""
        assert D14Software.crm_label == 'D14 Software'

    # ------------------------- #

    def test_inherits_from_d1(self) -> None:
        """Verify D14 inherits from D1 Digital Object;"""
        assert issubclass(D14Software, D1DigitalObject)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify D14 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(D14Software, E1CRMEntity)

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D14 can be instantiated with auto-generated ID;"""
        obj = D14Software()
        assert obj.id is not None
