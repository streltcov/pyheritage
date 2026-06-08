# -*- coding: utf-8 -*-

"""Tests for A1 Excavation Processing Unit;

A1 is declared with ABC — tested for metadata and MRO only;

"""

# pylint: disable=E0401,C0116,W0612

from abc import ABC

import pytest
from pydantic import ValidationError
from tests.cidoc.crmarchaeo.helpers import make_s4_kwargs

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E12Production,
    E64EndOfExistence,
)
from pyheritage.cidoc.crmarchaeo.entities import A1ExcavationProcessingUnit
from pyheritage.cidoc.crmarchaeo.properties import (
    AP1Produced,
    AP2Discarded,
    AP4ProducedSurface,
    AP5RemovedPartOrAll,
    AP6IntendedToApproximate,
    AP10Destroyed,
    AP32DiscardedInto,
)
from pyheritage.cidoc.crmsci.entities import S1MatterRemoval, S4Observation


class TestA1ExcavationProcessingUnit:

    def test_crm_code(self) -> None:
        """Verify CRM code is A1;"""
        assert A1ExcavationProcessingUnit.crm_code == 'A1'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label matches A1 Excavation Processing Unit;"""
        assert A1ExcavationProcessingUnit.crm_label == 'A1 Excavation Processing Unit'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify A1 is abstract (ABC in MRO);"""
        assert ABC in A1ExcavationProcessingUnit.__mro__

    # ------------------------- #

    def test_inherits_from_e12(self) -> None:
        """Verify A1 inherits from E12 Production;"""
        assert issubclass(A1ExcavationProcessingUnit, E12Production)

    # ------------------------- #

    def test_inherits_from_e64(self) -> None:
        """Verify A1 inherits from E64 End of Existence;"""
        assert issubclass(A1ExcavationProcessingUnit, E64EndOfExistence)

    # ------------------------- #

    def test_inherits_from_s1(self) -> None:
        """Verify A1 inherits from S1 Matter Removal;"""
        assert issubclass(A1ExcavationProcessingUnit, S1MatterRemoval)

    # ------------------------- #

    def test_inherits_from_s4(self) -> None:
        """Verify A1 inherits from S4 Observation;"""
        assert issubclass(A1ExcavationProcessingUnit, S4Observation)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify A1 inherits from E1 CRM Entity;"""
        assert issubclass(A1ExcavationProcessingUnit, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_ap1_produced(self) -> None:
        """Verify AP1 Produced mixin is in A1 MRO;"""
        assert AP1Produced in A1ExcavationProcessingUnit.__mro__

    # ------------------------- #

    def test_mro_includes_ap2_discarded(self) -> None:
        """Verify AP2 Discarded mixin is in A1 MRO;"""
        assert AP2Discarded in A1ExcavationProcessingUnit.__mro__

    # ------------------------- #

    def test_mro_includes_ap4_produced_surface(self) -> None:
        """Verify AP4 Produced Surface mixin is in A1 MRO;"""
        assert AP4ProducedSurface in A1ExcavationProcessingUnit.__mro__

    # ------------------------- #

    def test_mro_includes_ap5_removed_part_or_all(self) -> None:
        """Verify AP5 Removed Part or All mixin is in A1 MRO;"""
        assert AP5RemovedPartOrAll in A1ExcavationProcessingUnit.__mro__

    # ------------------------- #

    def test_ap5_rejects_empty_list(self) -> None:
        """Verify AP5 raises ValidationError for empty list (min_length=1);"""
        with pytest.raises(ValidationError):
            A1ExcavationProcessingUnit(
                ap5_removed_part_or_all=[],
                **make_s4_kwargs(),
            )

    # ------------------------- #

    def test_mro_includes_ap6_intended_to_approximate(self) -> None:
        """Verify AP6 Intended to Approximate mixin is in A1 MRO;"""
        assert AP6IntendedToApproximate in A1ExcavationProcessingUnit.__mro__

    # ------------------------- #

    def test_mro_includes_ap10_destroyed(self) -> None:
        """Verify AP10 Destroyed mixin is in A1 MRO;"""
        assert AP10Destroyed in A1ExcavationProcessingUnit.__mro__

    # ------------------------- #

    def test_ap10_rejects_empty_list(self) -> None:
        """Verify AP10 raises ValidationError for empty list (min_length=1);"""
        with pytest.raises(ValidationError):
            A1ExcavationProcessingUnit(
                ap10_destroyed=[],
                **make_s4_kwargs(),
            )

    # ------------------------- #

    def test_mro_includes_ap32_discarded_into(self) -> None:
        """Verify AP32 Discarded Into mixin is in A1 MRO;"""
        assert AP32DiscardedInto in A1ExcavationProcessingUnit.__mro__
