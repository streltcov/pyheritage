# -*- coding: utf-8 -*-

"""Tests for CRMinf belief-chain concrete entities (I10, I12, I13, I14);

These inherit from I2 Belief or I4 Proposition Set and carry belief-chain properties;

"""

# pylint: disable=E0401,C0116,W0612

import pytest
from pydantic import ValidationError
from tests.cidoc.crminf.helpers import (
    make_belief_value,
    make_minimal_i10,
    make_proposition_set,
)

from pyheritage.cidoc.core.entities import (
    E2TemporalEntity,
    E70Thing,
    E73InformationObject,
)
from pyheritage.cidoc.crminf.entities import (
    I2Belief,
    I4PropositionSet,
    I10ProvenanceStatement,
    I12AdoptedBelief,
    I13IntendedMeaningBelief,
    I14ProvenanceBelief,
)
from pyheritage.cidoc.crminf.properties import (
    J4That,
    J5HoldsToBe,
    J14AdoptedInterpretationOf,
    J16AssumedMeaning,
    J17About,
    J19That,
    J20IsAboutTheProvenanceOf,
)


class TestI10ProvenanceStatement:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I10';"""
        assert I10ProvenanceStatement.crm_code == 'I10'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I10 Provenance Statement';"""
        assert I10ProvenanceStatement.crm_label == 'I10 Provenance Statement'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I10 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I10ProvenanceStatement.__bases__

    # ------------------------- #

    def test_inherits_from_i4(self) -> None:
        """Checks that I10 inherits from I4 Proposition Set;"""
        assert issubclass(I10ProvenanceStatement, I4PropositionSet)

    # ------------------------- #

    def test_inherits_from_e73(self) -> None:
        """Checks that I10 inherits from E73 Information Object;"""
        assert issubclass(I10ProvenanceStatement, E73InformationObject)

    # ------------------------- #

    def test_mro_includes_j20(self) -> None:
        """Checks that J20 Is About The Provenance Of is in I10 MRO;"""
        assert J20IsAboutTheProvenanceOf in I10ProvenanceStatement.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Checks that @id is auto-generated on instantiation;"""
        entity = I10ProvenanceStatement(
            j20_is_about_the_provenance_of=[E70Thing()],
        )
        assert entity.id is not None

    # ------------------------- #

    def test_j20_accepts_e70(self) -> None:
        """Checks that J20 property accepts E70 Thing instances;"""
        thing = E70Thing()
        entity = I10ProvenanceStatement(
            j20_is_about_the_provenance_of=[thing],
        )
        assert entity.j20_is_about_the_provenance_of[0] is thing

    # ------------------------- #

    def test_j20_allows_empty(self) -> None:
        """J20 is optional (0,n);"""
        entity = I10ProvenanceStatement()
        assert entity.j20_is_about_the_provenance_of is None


# ******************************************************************************************************************* #


class TestI12AdoptedBelief:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I12';"""
        assert I12AdoptedBelief.crm_code == 'I12'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I12 Adopted Belief';"""
        assert I12AdoptedBelief.crm_label == 'I12 Adopted Belief'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I12 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I12AdoptedBelief.__bases__

    # ------------------------- #

    def test_inherits_from_i2(self) -> None:
        """Checks that I12 inherits from I2 Belief;"""
        assert issubclass(I12AdoptedBelief, I2Belief)

    # ------------------------- #

    def test_inherits_from_e2(self) -> None:
        """Checks that I12 inherits from E2 Temporal Entity;"""
        assert issubclass(I12AdoptedBelief, E2TemporalEntity)

    # ------------------------- #

    def test_mro_includes_j4(self) -> None:
        """Checks that J4 That is in I12 MRO (inherited from I2);"""
        assert J4That in I12AdoptedBelief.__mro__

    # ------------------------- #

    def test_mro_includes_j5(self) -> None:
        """Checks that J5 Holds To Be is in I12 MRO (inherited from I2);"""
        assert J5HoldsToBe in I12AdoptedBelief.__mro__

    # ------------------------- #

    def test_mro_includes_j14(self) -> None:
        """Checks that J14 Adopted Interpretation Of is in I12 MRO;"""
        assert J14AdoptedInterpretationOf in I12AdoptedBelief.__mro__

    # ------------------------- #

    def test_j14_accepts_e73(self) -> None:
        """Checks that J14 property accepts E73 Information Object instances;"""
        info = E73InformationObject()
        entity = I12AdoptedBelief(
            j14_adopted_interpretation_of=[info],
            j4_that=[make_proposition_set()],
            j5_holds_to_be=make_belief_value('True'),
        )
        assert entity.j14_adopted_interpretation_of[0] is info

    # ------------------------- #

    def test_j14_rejects_empty_list(self) -> None:
        """Checks that J14 (1,n) rejects an empty list;"""
        with pytest.raises(ValidationError):
            I12AdoptedBelief(
                j14_adopted_interpretation_of=[],
                j4_that=[make_proposition_set()],
                j5_holds_to_be=make_belief_value('True'),
            )


# ******************************************************************************************************************* #


class TestI13IntendedMeaningBelief:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I13';"""
        assert I13IntendedMeaningBelief.crm_code == 'I13'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I13 Intended Meaning Belief';"""
        assert I13IntendedMeaningBelief.crm_label == 'I13 Intended Meaning Belief'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I13 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I13IntendedMeaningBelief.__bases__

    # ------------------------- #

    def test_inherits_from_i2(self) -> None:
        """Checks that I13 inherits from I2 Belief;"""
        assert issubclass(I13IntendedMeaningBelief, I2Belief)

    # ------------------------- #

    def test_inherits_from_e2(self) -> None:
        """Checks that I13 inherits from E2 Temporal Entity;"""
        assert issubclass(I13IntendedMeaningBelief, E2TemporalEntity)

    # ------------------------- #

    def test_mro_includes_j4(self) -> None:
        """Checks that J4 That is in I13 MRO (inherited from I2);"""
        assert J4That in I13IntendedMeaningBelief.__mro__

    # ------------------------- #

    def test_mro_includes_j5(self) -> None:
        """Checks that J5 Holds To Be is in I13 MRO (inherited from I2);"""
        assert J5HoldsToBe in I13IntendedMeaningBelief.__mro__

    # ------------------------- #

    def test_mro_includes_j16(self) -> None:
        """Checks that J16 Assumed Meaning is in I13 MRO;"""
        assert J16AssumedMeaning in I13IntendedMeaningBelief.__mro__

    # ------------------------- #

    def test_mro_includes_j17(self) -> None:
        """Checks that J17 About is in I13 MRO;"""
        assert J17About in I13IntendedMeaningBelief.__mro__

    # ------------------------- #

    def test_j16_accepts_i4(self) -> None:
        """Checks that J16 property accepts I4 Proposition Set instances;"""
        prop = make_proposition_set()
        entity = I13IntendedMeaningBelief(
            j16_assumed_meaning=[prop],
            j17_about=[E73InformationObject()],
            j4_that=[make_proposition_set()],
            j5_holds_to_be=make_belief_value('True'),
        )
        assert entity.j16_assumed_meaning[0] is prop

    # ------------------------- #

    def test_j17_accepts_e73(self) -> None:
        """Checks that J17 property accepts E73 Information Object instances;"""
        info = E73InformationObject()
        entity = I13IntendedMeaningBelief(
            j16_assumed_meaning=[make_proposition_set()],
            j17_about=[info],
            j4_that=[make_proposition_set()],
            j5_holds_to_be=make_belief_value('True'),
        )
        assert entity.j17_about[0] is info

    # ------------------------- #

    def test_j16_rejects_empty_list(self) -> None:
        """Checks that J16 (1,n) rejects an empty list;"""
        with pytest.raises(ValidationError):
            I13IntendedMeaningBelief(
                j16_assumed_meaning=[],
                j17_about=[E73InformationObject()],
                j4_that=[make_proposition_set()],
                j5_holds_to_be=make_belief_value('True'),
            )

    # ------------------------- #

    def test_j17_rejects_empty_list(self) -> None:
        """Checks that J17 (1,n) rejects an empty list;"""
        with pytest.raises(ValidationError):
            I13IntendedMeaningBelief(
                j16_assumed_meaning=[make_proposition_set()],
                j17_about=[],
                j4_that=[make_proposition_set()],
                j5_holds_to_be=make_belief_value('True'),
            )


# ******************************************************************************************************************* #


class TestI14ProvenanceBelief:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I14';"""
        assert I14ProvenanceBelief.crm_code == 'I14'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I14 Provenance Belief';"""
        assert I14ProvenanceBelief.crm_label == 'I14 Provenance Belief'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I14 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I14ProvenanceBelief.__bases__

    # ------------------------- #

    def test_inherits_from_i2(self) -> None:
        """Checks that I14 inherits from I2 Belief;"""
        assert issubclass(I14ProvenanceBelief, I2Belief)

    # ------------------------- #

    def test_inherits_from_e2(self) -> None:
        """Checks that I14 inherits from E2 Temporal Entity;"""
        assert issubclass(I14ProvenanceBelief, E2TemporalEntity)

    # ------------------------- #

    def test_mro_includes_j4(self) -> None:
        """Checks that J4 That is in I14 MRO (inherited from I2);"""
        assert J4That in I14ProvenanceBelief.__mro__

    # ------------------------- #

    def test_mro_includes_j5(self) -> None:
        """Checks that J5 Holds To Be is in I14 MRO (inherited from I2);"""
        assert J5HoldsToBe in I14ProvenanceBelief.__mro__

    # ------------------------- #

    def test_mro_includes_j19(self) -> None:
        """Checks that J19 That is in I14 MRO;"""
        assert J19That in I14ProvenanceBelief.__mro__

    # ------------------------- #

    def test_j19_accepts_i10(self) -> None:
        """Checks that J19 property accepts I10 Provenance Statement instances;"""
        i10 = make_minimal_i10()
        entity = I14ProvenanceBelief(
            j19_that=[i10],
            j4_that=[make_proposition_set()],
            j5_holds_to_be=make_belief_value('True'),
        )
        assert entity.j19_that[0] is i10

    # ------------------------- #

    def test_j19_rejects_empty_list(self) -> None:
        """Checks that J19 (1,n) rejects an empty list;"""
        with pytest.raises(ValidationError):
            I14ProvenanceBelief(
                j19_that=[],
                j4_that=[make_proposition_set()],
                j5_holds_to_be=make_belief_value('True'),
            )
