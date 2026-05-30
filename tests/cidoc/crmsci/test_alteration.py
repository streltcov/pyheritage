# -*- coding: utf-8 -*-

"""Tests for CRMsci alteration hierarchy entities: S17, S18;

"""


# pylint: disable=E0401,C0116,W0612


from abc import ABC

from pyheritage.cidoc.core.entities import E1CRMEntity, E5Event, E63BeginningOfExistence
from pyheritage.cidoc.crmsci.entities import S17PhysicalGenesis, S18Alteration
from pyheritage.cidoc.crmsci.properties import O17Generated, O18Altered


class TestS18Alteration:
    """S18 Alteration entity tests;

    S18 is abstract class — no direct instantiation allowed;

    """

    def test_crm_code(self) -> None:
        """Verify S18 CRM code is 'S18';"""
        assert S18Alteration.crm_code == 'S18'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S18 CRM label is 'S18 Alteration';"""
        assert S18Alteration.crm_label == 'S18 Alteration'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify S18 is abstract and cannot be instantiated;"""
        assert ABC in S18Alteration.__mro__

    # ------------------------- #

    def test_inherits_from_e5(self) -> None:
        """Verify S18 inherits from E5 Event;"""
        assert issubclass(S18Alteration, E5Event)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S18 inherits from E1 CRM Entity;"""
        assert issubclass(S18Alteration, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o18_altered(self) -> None:
        """Verify O18Altered property mixin is present in S18 MRO;"""
        assert O18Altered in S18Alteration.__mro__

    # ------------------------- #

    def test_s17_is_subclass(self) -> None:
        """Verify S17PhysicalGenesis is a subclass of S18;"""
        assert issubclass(S17PhysicalGenesis, S18Alteration)


# ******************************************************************************************************************* #


class TestS17PhysicalGenesis:
    """S17 Physical Genesis entity tests;

    S17 is abstract class — no direct instantiation allowed;

    """

    def test_crm_code(self) -> None:
        """Verify S17 CRM code is 'S17'."""
        assert S17PhysicalGenesis.crm_code == 'S17'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S17 CRM label is 'S17 Physical Genesis';"""
        assert S17PhysicalGenesis.crm_label == 'S17 Physical Genesis'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify S17 is abstract and cannot be instantiated;"""
        assert ABC in S17PhysicalGenesis.__mro__

    # ------------------------- #

    def test_inherits_from_e63(self) -> None:
        """Verify S17 inherits from E63 Beginning of Existence;"""
        assert issubclass(S17PhysicalGenesis, E63BeginningOfExistence)

    # ------------------------- #

    def test_inherits_from_s18(self) -> None:
        """Verify S17 inherits from S18 Alteration;"""
        assert issubclass(S17PhysicalGenesis, S18Alteration)

    # ------------------------- #

    def test_inherits_from_e5(self) -> None:
        """Verify S17 inherits from E5 Event (through the chain);"""
        assert issubclass(S17PhysicalGenesis, E5Event)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S17 inherits from E1 CRM Entity;"""
        assert issubclass(S17PhysicalGenesis, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o17_generated(self) -> None:
        """Verify O17Generated property mixin is present in S17 MRO;"""
        assert O17Generated in S17PhysicalGenesis.__mro__

    # ------------------------- #

    def test_mro_includes_o18_altered(self) -> None:
        """Verify O18Altered property mixin is present in S17 MRO;"""
        assert O18Altered in S17PhysicalGenesis.__mro__
