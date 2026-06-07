"""Tests for A10 Excavation Interface;

A10 has no CRMArchaeo-specific properties — only CIDOC/CRMsci inherited ones.

"""

# pylint: disable=E0401,C0116,W0612

from tests.cidoc.crmarchaeo.helpers import make_a10

from pyheritage.cidoc.core.entities import E1CRMEntity, E25HumanMadeFeature
from pyheritage.cidoc.crmarchaeo.entities import A10ExcavationInterface
from pyheritage.cidoc.crmsci.entities import S20RigidPhysicalFeature


class TestA10ExcavationInterface:

    def test_crm_code(self) -> None:
        """Verify CRM code is A10;"""
        assert A10ExcavationInterface.crm_code == 'A10'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label matches A10 Excavation Interface;"""
        assert A10ExcavationInterface.crm_label == 'A10 Excavation Interface'

    # ------------------------- #

    def test_inherits_from_s20(self) -> None:
        """Verify A10 inherits from S20 Rigid Physical Feature;"""
        assert issubclass(A10ExcavationInterface, S20RigidPhysicalFeature)

    # ------------------------- #

    def test_inherits_from_e25(self) -> None:
        """Verify A10 inherits from E25 Human-Made Feature;"""
        assert issubclass(A10ExcavationInterface, E25HumanMadeFeature)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify A10 inherits from E1 CRM Entity;"""
        assert issubclass(A10ExcavationInterface, E1CRMEntity)

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify UUID @id is auto-generated on creation;"""
        entity = make_a10()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each instance gets a unique UUID;"""
        a = make_a10()
        b = make_a10()

        assert a.id != b.id

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify A10 can be created with an E41 Appellation;"""
        entity = make_a10('Planum 6 of square I22')
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Planum 6 of square I22'

    # ------------------------- #

    def test_model_dump_includes_id(self) -> None:
        """Verify model_dump includes id field;"""
        entity = make_a10()
        data = entity.model_dump()

        assert 'id' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization with by_alias includes @id;"""
        entity = make_a10('Planum 6')
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'Planum 6' in json_str
