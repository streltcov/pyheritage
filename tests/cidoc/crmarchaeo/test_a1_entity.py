"""Tests for A1 Excavation Processing Unit;

A1 is declared with ABC — tested for metadata and MRO only.

"""

# pylint: disable=E0401,C0116,W0612

from abc import ABC

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
        assert A1ExcavationProcessingUnit.crm_code == 'A1'

    def test_crm_label(self) -> None:
        assert A1ExcavationProcessingUnit.crm_label == 'A1 Excavation Processing Unit'

    def test_is_abstract(self) -> None:
        assert ABC in A1ExcavationProcessingUnit.__mro__

    def test_inherits_from_e12(self) -> None:
        assert issubclass(A1ExcavationProcessingUnit, E12Production)

    def test_inherits_from_e64(self) -> None:
        assert issubclass(A1ExcavationProcessingUnit, E64EndOfExistence)

    def test_inherits_from_s1(self) -> None:
        assert issubclass(A1ExcavationProcessingUnit, S1MatterRemoval)

    def test_inherits_from_s4(self) -> None:
        assert issubclass(A1ExcavationProcessingUnit, S4Observation)

    def test_inherits_from_e1(self) -> None:
        assert issubclass(A1ExcavationProcessingUnit, E1CRMEntity)

    def test_mro_includes_ap1_produced(self) -> None:
        assert AP1Produced in A1ExcavationProcessingUnit.__mro__

    def test_mro_includes_ap2_discarded(self) -> None:
        assert AP2Discarded in A1ExcavationProcessingUnit.__mro__

    def test_mro_includes_ap4_produced_surface(self) -> None:
        assert AP4ProducedSurface in A1ExcavationProcessingUnit.__mro__

    def test_mro_includes_ap5_removed_part_or_all(self) -> None:
        assert AP5RemovedPartOrAll in A1ExcavationProcessingUnit.__mro__

    def test_mro_includes_ap6_intended_to_approximate(self) -> None:
        assert AP6IntendedToApproximate in A1ExcavationProcessingUnit.__mro__

    def test_mro_includes_ap10_destroyed(self) -> None:
        assert AP10Destroyed in A1ExcavationProcessingUnit.__mro__

    def test_mro_includes_ap32_discarded_into(self) -> None:
        assert AP32DiscardedInto in A1ExcavationProcessingUnit.__mro__
