# -*- coding: utf-8 -*-

"""Tests for D35 Area;

"""

# pylint: disable=E0401,C0116,W0612

from pyheritage.cidoc.crmdig.entities import D1DigitalObject, D35Area
from pyheritage.cidoc.crmdig.properties import (
    L49IsPrimaryAreaOf,
    L50IsPropagatedArea,
)


class TestD35Area:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D35';"""
        assert D35Area.crm_code == 'D35'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D35 Area';"""
        assert D35Area.crm_label == 'D35 Area'

    # ------------------------- #

    def test_inherits_from_d1(self) -> None:
        """Verify D35 inherits from D1 Digital Object;"""
        assert issubclass(D35Area, D1DigitalObject)

    # ------------------------- #

    def test_mro_includes_l49(self) -> None:
        """Verify L49 (is primary area of) mixin is in D35 MRO;"""
        assert L49IsPrimaryAreaOf in D35Area.__mro__

    # ------------------------- #

    def test_mro_includes_l50(self) -> None:
        """Verify L50 (is propagated area) mixin is in D35 MRO;"""
        assert L50IsPropagatedArea in D35Area.__mro__

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D35 can be instantiated with auto-generated ID;"""
        obj = D35Area()
        assert obj.id is not None
