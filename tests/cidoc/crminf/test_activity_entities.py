# -*- coding: utf-8 -*-

"""Tests for CRMinf activity-based concrete entities (I5, I7, I15, I16, I17);

All inherit from I1 Argumentation (E7 Activity) and require activity kwargs;

"""

# pylint: disable=E0401,C0116,W0612

import pytest
from pydantic import ValidationError
from tests.cidoc.crminf.helpers import (
    make_activity_kwargs,
    make_e13_kwargs,
    make_minimal_i2,
    make_minimal_i12,
    make_minimal_i13,
    make_minimal_i14,
)

from pyheritage.cidoc.core.entities import (
    E7Activity,
    E13AttributeAssignment,
    E73InformationObject,
)
from pyheritage.cidoc.crminf.entities import (
    I1Argumentation,
    I3InferenceLogic,
    I5InferenceMaking,
    I7BeliefAdoption,
    I15ProvenanceAssessment,
    I16MeaningComprehension,
    I17CategoricalHypothesisBuilding,
)
from pyheritage.cidoc.crminf.properties import (
    J1UsedAsPremise,
    J2ConcludedThat,
    J3Applied,
    J7IsBasedOnEvidenceFrom,
    J13AdoptedInterpretation,
    J15AssumedMeaning,
    J18AssumedProvenance,
    J21ConcludedProvenance,
    J22InterpretedMeaningOf,
    J23InterpretedMeaningAs,
)


class TestI5InferenceMaking:

    KW = make_e13_kwargs('I5')

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I5';"""
        assert I5InferenceMaking.crm_code == 'I5'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I5 Inference Making';"""
        assert I5InferenceMaking.crm_label == 'I5 Inference Making'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I5 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I5InferenceMaking.__bases__

    # ------------------------- #

    def test_inherits_from_i1(self) -> None:
        """Checks that I5 inherits from I1 Argumentation;"""
        assert issubclass(I5InferenceMaking, I1Argumentation)

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Checks that I5 inherits from E13 Attribute Assignment;"""
        assert issubclass(I5InferenceMaking, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e7(self) -> None:
        """Checks that I5 ultimately inherits from E7 Activity;"""
        assert issubclass(I5InferenceMaking, E7Activity)

    # ------------------------- #

    def test_mro_includes_j1(self) -> None:
        """Checks that J1 Used As Premise is in I5 MRO;"""
        assert J1UsedAsPremise in I5InferenceMaking.__mro__

    # ------------------------- #

    def test_mro_includes_j3(self) -> None:
        """Checks that J3 Applied is in I5 MRO;"""
        assert J3Applied in I5InferenceMaking.__mro__

    # ------------------------- #

    def test_mro_includes_j2(self) -> None:
        """J2 inherited from I1;"""
        assert J2ConcludedThat in I5InferenceMaking.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Checks that @id is auto-generated on instantiation;"""
        entity = I5InferenceMaking(
            **self.KW,
            j1_used_as_premise=[make_minimal_i2()],
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[I3InferenceLogic()],
        )
        assert entity.id is not None

    # ------------------------- #

    def test_j1_accepts_i2(self) -> None:
        """Checks that J1 property accepts I2 Belief instances;"""
        i2 = make_minimal_i2()
        entity = I5InferenceMaking(
            **self.KW,
            j1_used_as_premise=[i2],
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[I3InferenceLogic()],
        )
        assert entity.j1_used_as_premise[0] is i2

    # ------------------------- #

    def test_j3_accepts_i3(self) -> None:
        """Checks that J3 property accepts I3 Inference Logic instances;"""
        logic = I3InferenceLogic()
        entity = I5InferenceMaking(
            **self.KW,
            j1_used_as_premise=[make_minimal_i2()],
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[logic],
        )
        assert entity.j3_applied[0] is logic

    # ------------------------- #

    def test_j1_allows_empty_list(self) -> None:
        """J1 is optional (0,n) — empty list is valid;"""
        entity = I5InferenceMaking(
            **self.KW,
            j1_used_as_premise=[],
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[I3InferenceLogic()],
        )
        assert entity.j1_used_as_premise is not None
        assert len(entity.j1_used_as_premise) == 0

    # ------------------------- #

    def test_j3_rejects_empty_list(self) -> None:
        """Checks that J3 (1,n) rejects an empty list;"""
        with pytest.raises(ValidationError):
            I5InferenceMaking(
                **self.KW,
                j1_used_as_premise=[make_minimal_i2()],
                j2_concluded_that=[make_minimal_i2()],
                j3_applied=[],
            )

    # ------------------------- #

    def test_j2_inherited_from_i1(self) -> None:
        """Checks that J2 is accessible on I5 via I1 inheritance;"""
        entity = I5InferenceMaking(
            **self.KW,
            j1_used_as_premise=[make_minimal_i2()],
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[I3InferenceLogic()],
        )
        assert hasattr(entity, 'j2_concluded_that')

    # ------------------------- #

    def test_model_dump_includes_fields(self) -> None:
        """Checks that model_dump includes J1 and J3 fields;"""
        entity = I5InferenceMaking(
            **self.KW,
            j1_used_as_premise=[make_minimal_i2()],
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[I3InferenceLogic()],
        )
        data = entity.model_dump()

        assert 'j1_used_as_premise' in data
        assert 'j3_applied' in data


# ******************************************************************************************************************* #


class TestI7BeliefAdoption:

    KW = make_activity_kwargs('I7')

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I7';"""
        assert I7BeliefAdoption.crm_code == 'I7'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I7 Belief Adoption';"""
        assert I7BeliefAdoption.crm_label == 'I7 Belief Adoption'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I7 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I7BeliefAdoption.__bases__

    # ------------------------- #

    def test_inherits_from_i1(self) -> None:
        """Checks that I7 inherits from I1 Argumentation;"""
        assert issubclass(I7BeliefAdoption, I1Argumentation)

    # ------------------------- #

    def test_inherits_from_e7(self) -> None:
        """Checks that I7 ultimately inherits from E7 Activity;"""
        assert issubclass(I7BeliefAdoption, E7Activity)

    # ------------------------- #

    def test_mro_includes_j7(self) -> None:
        """Checks that J7 Is Based On Evidence From is in I7 MRO;"""
        assert J7IsBasedOnEvidenceFrom in I7BeliefAdoption.__mro__

    # ------------------------- #

    def test_mro_includes_j13(self) -> None:
        """Checks that J13 Adopted Interpretation is in I7 MRO;"""
        assert J13AdoptedInterpretation in I7BeliefAdoption.__mro__

    # ------------------------- #

    def test_mro_includes_j15(self) -> None:
        """Checks that J15 Assumed Meaning is in I7 MRO;"""
        assert J15AssumedMeaning in I7BeliefAdoption.__mro__

    # ------------------------- #

    def test_mro_includes_j18(self) -> None:
        """Checks that J18 Assumed Provenance is in I7 MRO;"""
        assert J18AssumedProvenance in I7BeliefAdoption.__mro__

    # ------------------------- #

    def test_mro_includes_j2(self) -> None:
        """Checks that J2 Concluded That is in I7 MRO (inherited from I1);"""
        assert J2ConcludedThat in I7BeliefAdoption.__mro__

    # ------------------------- #

    def test_j7_accepts_e73(self) -> None:
        """Checks that J7 property accepts E73 Information Object instances;"""
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

    def test_j13_accepts_i12(self) -> None:
        """Checks that J13 property accepts I12 Adopted Belief instances;"""
        i12 = make_minimal_i12()
        entity = I7BeliefAdoption(
            **self.KW,
            j7_is_based_on_evidence_from=[E73InformationObject()],
            j13_adopted_interpretation=[i12],
            j15_assumed_meaning=[make_minimal_i13()],
            j18_assumed_provenance=[make_minimal_i14()],
            j2_concluded_that=[make_minimal_i2()],
        )
        assert entity.j13_adopted_interpretation[0] is i12

    # ------------------------- #

    def test_j15_accepts_i13(self) -> None:
        """Checks that J15 property accepts I13 Intended Meaning Belief instances;"""
        i13 = make_minimal_i13()
        entity = I7BeliefAdoption(
            **self.KW,
            j7_is_based_on_evidence_from=[E73InformationObject()],
            j13_adopted_interpretation=[make_minimal_i12()],
            j15_assumed_meaning=[i13],
            j18_assumed_provenance=[make_minimal_i14()],
            j2_concluded_that=[make_minimal_i2()],
        )
        assert entity.j15_assumed_meaning[0] is i13

    # ------------------------- #

    def test_j18_accepts_i14(self) -> None:
        """Checks that J18 property accepts I14 Provenance Belief instances;"""
        i14 = make_minimal_i14()
        entity = I7BeliefAdoption(
            **self.KW,
            j7_is_based_on_evidence_from=[E73InformationObject()],
            j13_adopted_interpretation=[make_minimal_i12()],
            j15_assumed_meaning=[make_minimal_i13()],
            j18_assumed_provenance=[i14],
            j2_concluded_that=[make_minimal_i2()],
        )
        assert entity.j18_assumed_provenance[0] is i14

    # ------------------------- #

    def test_j7_rejects_empty_list(self) -> None:
        """Checks that J7 (1,n) rejects an empty list;"""
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


class TestI15ProvenanceAssessment:

    KW = make_activity_kwargs('I15')

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I15';"""
        assert I15ProvenanceAssessment.crm_code == 'I15'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I15 Provenance Assessment';"""
        assert I15ProvenanceAssessment.crm_label == 'I15 Provenance Assessment'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I15 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I15ProvenanceAssessment.__bases__

    # ------------------------- #

    def test_inherits_from_i1(self) -> None:
        """Checks that I15 inherits from I1 Argumentation;"""
        assert issubclass(I15ProvenanceAssessment, I1Argumentation)

    # ------------------------- #

    def test_inherits_from_e7(self) -> None:
        """Checks that I15 ultimately inherits from E7 Activity;"""
        assert issubclass(I15ProvenanceAssessment, E7Activity)

    # ------------------------- #

    def test_mro_includes_j21(self) -> None:
        """Checks that J21 Concluded Provenance is in I15 MRO;"""
        assert J21ConcludedProvenance in I15ProvenanceAssessment.__mro__

    # ------------------------- #

    def test_mro_includes_j2(self) -> None:
        """Checks that J2 Concluded That is in I15 MRO (inherited from I1);"""
        assert J2ConcludedThat in I15ProvenanceAssessment.__mro__

    # ------------------------- #

    def test_j21_accepts_i14(self) -> None:
        """Checks that J21 property accepts I14 Provenance Belief instances;"""
        i14 = make_minimal_i14()
        entity = I15ProvenanceAssessment(
            **self.KW,
            j21_concluded_provenance=[i14],
            j2_concluded_that=[make_minimal_i2()],
        )
        assert entity.j21_concluded_provenance[0] is i14

    # ------------------------- #

    def test_j21_rejects_empty_list(self) -> None:
        """Checks that J21 (1,n) rejects an empty list;"""
        with pytest.raises(ValidationError):
            I15ProvenanceAssessment(
                **self.KW,
                j21_concluded_provenance=[],
                j2_concluded_that=[make_minimal_i2()],
            )


# ******************************************************************************************************************* #


class TestI16MeaningComprehension:

    KW = make_activity_kwargs('I16')

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I16';"""
        assert I16MeaningComprehension.crm_code == 'I16'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I16 Meaning Comprehension';"""
        assert I16MeaningComprehension.crm_label == 'I16 Meaning Comprehension'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I16 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I16MeaningComprehension.__bases__

    # ------------------------- #

    def test_inherits_from_i1(self) -> None:
        """Checks that I16 inherits from I1 Argumentation;"""
        assert issubclass(I16MeaningComprehension, I1Argumentation)

    # ------------------------- #

    def test_inherits_from_e7(self) -> None:
        """Checks that I16 ultimately inherits from E7 Activity;"""
        assert issubclass(I16MeaningComprehension, E7Activity)

    # ------------------------- #

    def test_mro_includes_j22(self) -> None:
        """Checks that J22 Interpreted Meaning Of is in I16 MRO;"""
        assert J22InterpretedMeaningOf in I16MeaningComprehension.__mro__

    # ------------------------- #

    def test_mro_includes_j23(self) -> None:
        """Checks that J23 Interpreted Meaning As is in I16 MRO;"""
        assert J23InterpretedMeaningAs in I16MeaningComprehension.__mro__

    # ------------------------- #

    def test_mro_includes_j2(self) -> None:
        """Checks that J2 Concluded That is in I16 MRO (inherited from I1);"""
        assert J2ConcludedThat in I16MeaningComprehension.__mro__

    # ------------------------- #

    def test_j22_accepts_e73(self) -> None:
        """Checks that J22 property accepts E73 Information Object instances;"""
        entity = I16MeaningComprehension(
            **self.KW,
            j22_interpreted_meaning_of=[E73InformationObject()],
            j23_interpreted_meaning_as=[make_minimal_i13()],
            j2_concluded_that=[make_minimal_i2()],
        )
        assert len(entity.j22_interpreted_meaning_of) == 1

    # ------------------------- #

    def test_j23_accepts_i13(self) -> None:
        """Checks that J23 property accepts I13 Intended Meaning Belief instances;"""
        i13 = make_minimal_i13()
        entity = I16MeaningComprehension(
            **self.KW,
            j22_interpreted_meaning_of=[E73InformationObject()],
            j23_interpreted_meaning_as=[i13],
            j2_concluded_that=[make_minimal_i2()],
        )
        assert entity.j23_interpreted_meaning_as[0] is i13

    # ------------------------- #

    def test_j22_rejects_empty_list(self) -> None:
        """Checks that J22 (1,n) rejects an empty list;"""
        with pytest.raises(ValidationError):
            I16MeaningComprehension(
                **self.KW,
                j22_interpreted_meaning_of=[],
                j23_interpreted_meaning_as=[make_minimal_i13()],
                j2_concluded_that=[make_minimal_i2()],
            )

    # ------------------------- #

    def test_j23_rejects_empty_list(self) -> None:
        """Checks that J23 (1,n) rejects an empty list;"""
        with pytest.raises(ValidationError):
            I16MeaningComprehension(
                **self.KW,
                j22_interpreted_meaning_of=[E73InformationObject()],
                j23_interpreted_meaning_as=[],
                j2_concluded_that=[make_minimal_i2()],
            )


# ******************************************************************************************************************* #


class TestI17CategoricalHypothesisBuilding:

    KW = make_e13_kwargs('I17')

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I17';"""
        assert I17CategoricalHypothesisBuilding.crm_code == 'I17'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I17 Categorical Hypothesis Building';"""
        assert I17CategoricalHypothesisBuilding.crm_label == 'I17 Categorical Hypothesis Building'

    # ------------------------- #

    def test_is_not_abstract(self) -> None:
        """Checks that I17 is a concrete (non-abstract) entity;"""
        from abc import ABC
        assert ABC not in I17CategoricalHypothesisBuilding.__bases__

    # ------------------------- #

    def test_inherits_from_i5(self) -> None:
        """Checks that I17 inherits from I5 Inference Making;"""
        assert issubclass(I17CategoricalHypothesisBuilding, I5InferenceMaking)

    # ------------------------- #

    def test_inherits_from_i1(self) -> None:
        """Checks that I17 inherits from I1 Argumentation;"""
        assert issubclass(I17CategoricalHypothesisBuilding, I1Argumentation)

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Checks that I17 inherits from E13 Attribute Assignment;"""
        assert issubclass(I17CategoricalHypothesisBuilding, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e7(self) -> None:
        """Checks that I17 ultimately inherits from E7 Activity;"""
        assert issubclass(I17CategoricalHypothesisBuilding, E7Activity)

    # ------------------------- #

    def test_j1_available(self) -> None:
        """Checks that J1 property is available on I17 via I5 inheritance;"""
        entity = I17CategoricalHypothesisBuilding(
            **self.KW,
            j1_used_as_premise=[make_minimal_i2()],
            j2_concluded_that=[make_minimal_i2()],
            j3_applied=[I3InferenceLogic()],
        )
        assert hasattr(entity, 'j1_used_as_premise')
