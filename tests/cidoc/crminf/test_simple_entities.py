# -*- coding: utf-8 -*-

"""Tests for CRMinf simple concrete entities (I3, I6, I11);

These entities have no J-properties and minimal required fields;

"""

# pylint: disable=E0401,C0116,W0612

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E59PrimitiveValue,
    E73InformationObject,
    E89PropositionalObject,
)
from pyheritage.cidoc.crminf.entities import (
    I3InferenceLogic,
    I4PropositionSet,
    I6BeliefValue,
    I11Situation,
)


class TestI3InferenceLogic:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I3';"""
        assert I3InferenceLogic.crm_code == 'I3'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I3 Inference Logic';"""
        assert I3InferenceLogic.crm_label == 'I3 Inference Logic'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I3 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I3InferenceLogic.__bases__

    # ------------------------- #

    def test_inherits_from_e89(self) -> None:
        """Checks that I3 inherits from E89 Propositional Object;"""
        assert issubclass(I3InferenceLogic, E89PropositionalObject)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Checks that I3 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(I3InferenceLogic, E1CRMEntity)

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Checks that @id is auto-generated on instantiation;"""
        entity = I3InferenceLogic()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Checks that each instance receives a unique @id;"""
        a = I3InferenceLogic()
        b = I3InferenceLogic()

        assert a.id != b.id

    # ------------------------- #

    def test_model_dump_includes_id(self) -> None:
        """Checks that model_dump with by_alias includes @id;"""
        entity = I3InferenceLogic()
        data = entity.model_dump(by_alias=True)

        assert '@id' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Checks that @id appears in JSON serialization output;"""
        entity = I3InferenceLogic()
        json_str = entity.model_dump_json()

        assert entity.id in json_str


# ******************************************************************************************************************* #


class TestI6BeliefValue:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I6';"""
        assert I6BeliefValue.crm_code == 'I6'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I6 Belief Value';"""
        assert I6BeliefValue.crm_label == 'I6 Belief Value'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I6 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I6BeliefValue.__bases__

    # ------------------------- #

    def test_inherits_from_e59(self) -> None:
        """Checks that I6 inherits from E59 Primitive Value;"""
        assert issubclass(I6BeliefValue, E59PrimitiveValue)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Checks that I6 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(I6BeliefValue, E1CRMEntity)

    # ------------------------- #

    def test_default_value(self) -> None:
        """Checks that default value is 'Unknown';"""
        entity = I6BeliefValue()
        assert entity.value == 'Unknown'

    # ------------------------- #

    def test_custom_value(self) -> None:
        """Checks that a custom value can be set;"""
        entity = I6BeliefValue(value='True')
        assert entity.value == 'True'

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Checks that @id is auto-generated on instantiation;"""
        entity = I6BeliefValue()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Checks that each instance receives a unique @id;"""
        a = I6BeliefValue()
        b = I6BeliefValue()

        assert a.id != b.id

    # ------------------------- #

    def test_repr(self) -> None:
        """Checks that repr includes the belief value;"""
        entity = I6BeliefValue(value='False')
        assert 'False' in repr(entity)


# ******************************************************************************************************************* #


class TestI11Situation:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I11';"""
        assert I11Situation.crm_code == 'I11'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I11 Situation';"""
        assert I11Situation.crm_label == 'I11 Situation'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I11 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I11Situation.__bases__

    # ------------------------- #

    def test_inherits_from_i4(self) -> None:
        """Checks that I11 inherits from I4 Proposition Set;"""
        assert issubclass(I11Situation, I4PropositionSet)

    # ------------------------- #

    def test_inherits_from_e73(self) -> None:
        """Checks that I11 inherits from E73 Information Object;"""
        assert issubclass(I11Situation, E73InformationObject)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Checks that I11 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(I11Situation, E1CRMEntity)

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Checks that @id is auto-generated on instantiation;"""
        entity = I11Situation()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Checks that each instance receives a unique @id;"""
        a = I11Situation()
        b = I11Situation()

        assert a.id != b.id
