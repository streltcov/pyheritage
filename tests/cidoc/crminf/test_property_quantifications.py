# -*- coding: utf-8 -*-

"""Tests for CRMinf J-property quantifications and validation;

Verifies that each property field has the correct min_length, scalar/optional nature,
and rejects invalid inputs per the spec quantification;

"""

# pylint: disable=E0401,C0116,W0612

import pytest
from pydantic import ValidationError
from tests.cidoc.crminf.helpers import (
    make_activity_kwargs,
    make_belief_value,
    make_e13_kwargs,
    make_minimal_i2,
    make_minimal_i10,
    make_minimal_i12,
    make_minimal_i13,
    make_minimal_i14,
    make_proposition_set,
)

from pyheritage.cidoc.core.entities import E70Thing, E73InformationObject
from pyheritage.cidoc.crminf.entities import (
    I2Belief,
    I3InferenceLogic,
    I5InferenceMaking,
    I6BeliefValue,
    I7BeliefAdoption,
    I10ProvenanceStatement,
    I12AdoptedBelief,
    I13IntendedMeaningBelief,
    I14ProvenanceBelief,
    I15ProvenanceAssessment,
    I16MeaningComprehension,
)


class TestJ1Quantification:
    """J1: many to many (0,n:0,n) — optional list, no min_length;"""

    KW = make_e13_kwargs('J1')

    def test_j1_is_optional(self) -> None:
        """J1 (0,n) — can be omitted entirely;"""
        entity = I5InferenceMaking(
            **self.KW,
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[I3InferenceLogic()],
        )
        assert entity.j1_used_as_premise is None

    # ------------------------- #

    def test_j1_accepts_list(self) -> None:
        """J1 (0,n) — accepts a populated list;"""
        entity = I5InferenceMaking(
            **self.KW,
            j1_used_as_premise=[make_minimal_i2()],
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[I3InferenceLogic()],
        )
        assert entity.j1_used_as_premise is not None


class TestJ2Quantification:
    """J2: one to many, necessary, dependent (1,n:1,1) — List with min_length=1;"""

    KW = make_e13_kwargs('J2')

    def test_j2_accepts_i2(self) -> None:
        """J2 (1,n:1,1) — accepts I2 Belief instances;"""
        entity = I5InferenceMaking(
            **self.KW,
            j1_used_as_premise=[make_minimal_i2()],
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[I3InferenceLogic()],
        )
        assert len(entity.j2_concluded_that) == 1

    # ------------------------- #

    def test_j2_rejects_empty(self) -> None:
        """J2 (1,n:1,1) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I5InferenceMaking(
                **self.KW,
                j1_used_as_premise=[make_minimal_i2()],
                j2_concluded_that=[],
                j3_applied=[I3InferenceLogic()],
            )


# ******************************************************************************************************************* #


class TestJ3Quantification:
    """J3: many to many, necessary (1,n:0,1) — List with min_length=1;"""

    KW = make_e13_kwargs('J3')

    def test_j3_accepts_i3(self) -> None:
        """J3 (1,n:0,1) — accepts I3 Inference Logic instances;"""
        entity = I5InferenceMaking(
            **self.KW,
            j1_used_as_premise=[make_minimal_i2()],
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[I3InferenceLogic()],
        )
        assert len(entity.j3_applied) == 1

    # ------------------------- #

    def test_j3_rejects_empty(self) -> None:
        """J3 (1,n:0,1) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I5InferenceMaking(
                **self.KW,
                j1_used_as_premise=[make_minimal_i2()],
                j2_concluded_that=[make_minimal_i2()],
                j3_applied=[],
            )


# ******************************************************************************************************************* #


class TestJ4Quantification:
    """J4: many to many, necessary (1,n:0,n) — List with min_length=1;"""

    def test_j4_accepts_i4(self) -> None:
        """J4 (1,n:0,n) — accepts I4 Proposition Set instances;"""
        entity = I2Belief(
            j4_that=[make_proposition_set()],
            j5_holds_to_be=make_belief_value('True'),
        )
        assert len(entity.j4_that) == 1

    # ------------------------- #

    def test_j4_rejects_empty(self) -> None:
        """J4 (1,n:0,n) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I2Belief(
                j4_that=[],
                j5_holds_to_be=make_belief_value('True'),
            )


# ******************************************************************************************************************* #


class TestJ5Quantification:
    """J5: many to one, necessary (1,1:0,n) — scalar, required, not Optional;"""

    def test_j5_is_scalar(self) -> None:
        """J5 (1,1:0,n) — is a scalar (non-list) field;"""
        entity = I2Belief(
            j4_that=[make_proposition_set()],
            j5_holds_to_be=I6BeliefValue(value='True'),
        )
        assert isinstance(entity.j5_holds_to_be, I6BeliefValue)

    # ------------------------- #

    def test_j5_is_required(self) -> None:
        """J5 (1,1:0,n) — is required and raises error when missing;"""
        with pytest.raises(ValidationError):
            I2Belief(j4_that=[make_proposition_set()])

    # ------------------------- #

    def test_j5_rejects_wrong_type(self) -> None:
        """J5 (1,1:0,n) — rejects values of the wrong type;"""
        with pytest.raises(ValidationError):
            I2Belief(
                j4_that=[make_proposition_set()],
                j5_holds_to_be='not_a_belief_value',
            )


# ******************************************************************************************************************* #


class TestJ7Quantification:
    """J7: many to many, necessary (1,n:0,n) — List with min_length=1;"""

    KW = make_activity_kwargs('J7')

    def test_j7_accepts_e73(self) -> None:
        """J7 (1,n:0,n) — accepts E73 Information Object instances;"""
        entity = I7BeliefAdoption(
            **self.KW,
            j7_is_based_on_evidence_from=[E73InformationObject()],
            j13_adopted_interpretation=[make_minimal_i12()],
            j15_assumed_meaning=[make_minimal_i13()],
            j18_assumed_provenance=[make_minimal_i14()],
            j2_concluded_that=[make_minimal_i2()],
        )
        assert len(entity.j7_is_based_on_evidence_from) == 1

    # ------------------------- #

    def test_j7_rejects_empty(self) -> None:
        """J7 (1,n:0,n) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I7BeliefAdoption(
                **self.KW,
                j7_is_based_on_evidence_from=[],
                j13_adopted_interpretation=[make_minimal_i12()],
                j15_assumed_meaning=[make_minimal_i13()],
                j18_assumed_provenance=[make_minimal_i14()],
                j2_concluded_that=[make_minimal_i2()],
            )


# ******************************************************************************************************************* #


class TestJ14Quantification:
    """J14: many to many, necessary (1,n:0,n) — List with min_length=1;"""

    def test_j14_accepts_e73(self) -> None:
        """J14 (1,n:0,n) — accepts E73 Information Object instances;"""
        entity = I12AdoptedBelief(
            j14_adopted_interpretation_of=[E73InformationObject()],
            j4_that=[make_proposition_set()],
            j5_holds_to_be=make_belief_value('True'),
        )
        assert len(entity.j14_adopted_interpretation_of) == 1

    # ------------------------- #

    def test_j14_rejects_empty(self) -> None:
        """J14 (1,n:0,n) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I12AdoptedBelief(
                j14_adopted_interpretation_of=[],
                j4_that=[make_proposition_set()],
                j5_holds_to_be=make_belief_value('True'),
            )


# ******************************************************************************************************************* #


class TestJ16Quantification:
    """J16: many to many, necessary (1,n:0,n) — List with min_length=1;"""

    def test_j16_accepts_i4(self) -> None:
        """J16 (1,n:0,n) — accepts I4 Proposition Set instances;"""
        entity = I13IntendedMeaningBelief(
            j16_assumed_meaning=[make_proposition_set()],
            j17_about=[E73InformationObject()],
            j4_that=[make_proposition_set()],
            j5_holds_to_be=make_belief_value('True'),
        )
        assert len(entity.j16_assumed_meaning) == 1

    # ------------------------- #

    def test_j16_rejects_empty(self) -> None:
        """J16 (1,n:0,n) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I13IntendedMeaningBelief(
                j16_assumed_meaning=[],
                j17_about=[E73InformationObject()],
                j4_that=[make_proposition_set()],
                j5_holds_to_be=make_belief_value('True'),
            )


# ******************************************************************************************************************* #


class TestJ17Quantification:
    """J17: many to many, necessary (1,n:0,n) — List with min_length=1;"""

    def test_j17_accepts_e73(self) -> None:
        """J17 (1,n:0,n) — accepts E73 Information Object instances;"""
        entity = I13IntendedMeaningBelief(
            j16_assumed_meaning=[make_proposition_set()],
            j17_about=[E73InformationObject()],
            j4_that=[make_proposition_set()],
            j5_holds_to_be=make_belief_value('True'),
        )
        assert len(entity.j17_about) == 1

    # ------------------------- #

    def test_j17_rejects_empty(self) -> None:
        """J17 (1,n:0,n) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I13IntendedMeaningBelief(
                j16_assumed_meaning=[make_proposition_set()],
                j17_about=[],
                j4_that=[make_proposition_set()],
                j5_holds_to_be=make_belief_value('True'),
            )


# ******************************************************************************************************************* #


class TestJ19Quantification:
    """J19: many to many, necessary (1,n:0,n) — List with min_length=1;"""

    def test_j19_accepts_i10(self) -> None:
        """J19 (1,n:0,n) — accepts I10 Provenance Statement instances;"""
        entity = I14ProvenanceBelief(
            j19_that=[make_minimal_i10()],
            j4_that=[make_proposition_set()],
            j5_holds_to_be=make_belief_value('True'),
        )
        assert len(entity.j19_that) == 1

    # ------------------------- #

    def test_j19_rejects_empty(self) -> None:
        """J19 (1,n:0,n) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I14ProvenanceBelief(
                j19_that=[],
                j4_that=[make_proposition_set()],
                j5_holds_to_be=make_belief_value('True'),
            )


# ******************************************************************************************************************* #


class TestJ20Quantification:
    """J20: many to many (0,n:0,n) — optional list, no min_length;"""

    def test_j20_is_optional(self) -> None:
        """J20 (0,n:0,n) — can be omitted entirely;"""
        entity = I10ProvenanceStatement()
        assert entity.j20_is_about_the_provenance_of is None

    # ------------------------- #

    def test_j20_accepts_e70(self) -> None:
        """J20 (0,n:0,n) — accepts E70 Thing instances;"""
        entity = I10ProvenanceStatement(
            j20_is_about_the_provenance_of=[E70Thing()],
        )
        assert len(entity.j20_is_about_the_provenance_of) == 1


# ******************************************************************************************************************* #


class TestJ21Quantification:
    """J21: many to many, necessary (1,n:0,n) — List with min_length=1;"""

    KW = make_activity_kwargs('J21')

    def test_j21_accepts_i14(self) -> None:
        """J21 (1,n:0,n) — accepts I14 Provenance Belief instances;"""
        entity = I15ProvenanceAssessment(
            **self.KW,
            j21_concluded_provenance=[make_minimal_i14()],
            j2_concluded_that=[make_minimal_i2()],
        )
        assert len(entity.j21_concluded_provenance) == 1

    # ------------------------- #

    def test_j21_rejects_empty(self) -> None:
        """J21 (1,n:0,n) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I15ProvenanceAssessment(
                **self.KW,
                j21_concluded_provenance=[],
                j2_concluded_that=[make_minimal_i2()],
            )


# ******************************************************************************************************************* #


class TestJ22Quantification:
    """J22: many to many, necessary (1,n:0,n) — List with min_length=1;"""

    KW = make_activity_kwargs('J22')

    def test_j22_accepts_e73(self) -> None:
        """J22 (1,n:0,n) — accepts E73 Information Object instances;"""
        entity = I16MeaningComprehension(
            **self.KW,
            j22_interpreted_meaning_of=[E73InformationObject()],
            j23_interpreted_meaning_as=[make_minimal_i13()],
            j2_concluded_that=[make_minimal_i2()],
        )
        assert len(entity.j22_interpreted_meaning_of) == 1

    # ------------------------- #

    def test_j22_rejects_empty(self) -> None:
        """J22 (1,n:0,n) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I16MeaningComprehension(
                **self.KW,
                j22_interpreted_meaning_of=[],
                j23_interpreted_meaning_as=[make_minimal_i13()],
                j2_concluded_that=[make_minimal_i2()],
            )


# ******************************************************************************************************************* #


class TestJ23Quantification:
    """J23: one to many, necessary, dependent (1,n:1,1) — List with min_length=1;"""

    KW = make_activity_kwargs('J23')

    def test_j23_accepts_i13(self) -> None:
        """J23 (1,n:1,1) — accepts I13 Intended Meaning Belief instances;"""
        entity = I16MeaningComprehension(
            **self.KW,
            j22_interpreted_meaning_of=[E73InformationObject()],
            j23_interpreted_meaning_as=[make_minimal_i13()],
            j2_concluded_that=[make_minimal_i2()],
        )
        assert len(entity.j23_interpreted_meaning_as) == 1

    # ------------------------- #

    def test_j23_rejects_empty(self) -> None:
        """J23 (1,n:1,1) — rejects an empty list;"""
        with pytest.raises(ValidationError):
            I16MeaningComprehension(
                **self.KW,
                j22_interpreted_meaning_of=[E73InformationObject()],
                j23_interpreted_meaning_as=[],
                j2_concluded_that=[make_minimal_i2()],
            )
