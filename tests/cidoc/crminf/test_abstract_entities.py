# -*- coding: utf-8 -*-

"""Tests for CRMinf abstract entities (I1, I2, I4);

Abstract entities are tested for metadata, inheritance, and MRO only;

"""

# pylint: disable=E0401,C0116,W0612

from abc import ABC

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E2TemporalEntity,
    E7Activity,
    E73InformationObject,
)
from pyheritage.cidoc.crminf.entities import (
    I1Argumentation,
    I2Belief,
    I4PropositionSet,
)
from pyheritage.cidoc.crminf.properties import (
    J2ConcludedThat,
    J4That,
    J5HoldsToBe,
)


class TestI1Argumentation:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I1';"""
        assert I1Argumentation.crm_code == 'I1'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I1 Argumentation';"""
        assert I1Argumentation.crm_label == 'I1 Argumentation'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Checks that I1 is an abstract entity;"""
        assert ABC in I1Argumentation.__bases__

    # ------------------------- #

    def test_inherits_from_e7(self) -> None:
        """Checks that I1 inherits from E7 Activity;"""
        assert issubclass(I1Argumentation, E7Activity)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Checks that I1 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(I1Argumentation, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_j2(self) -> None:
        """Checks that J2 Concluded That is in I1 MRO;"""
        assert J2ConcludedThat in I1Argumentation.__mro__


# ******************************************************************************************************************* #


class TestI2Belief:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I2';"""
        assert I2Belief.crm_code == 'I2'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I2 Belief';"""
        assert I2Belief.crm_label == 'I2 Belief'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Checks that I2 is an abstract entity;"""
        assert ABC in I2Belief.__bases__

    # ------------------------- #

    def test_inherits_from_e2(self) -> None:
        """Checks that I2 inherits from E2 Temporal Entity;"""
        assert issubclass(I2Belief, E2TemporalEntity)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Checks that I2 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(I2Belief, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_j4(self) -> None:
        """Checks that J4 That is in I2 MRO;"""
        assert J4That in I2Belief.__mro__

    # ------------------------- #

    def test_mro_includes_j5(self) -> None:
        """Checks that J5 Holds To Be is in I2 MRO;"""
        assert J5HoldsToBe in I2Belief.__mro__


# ******************************************************************************************************************* #


class TestI4PropositionSet:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'I4';"""
        assert I4PropositionSet.crm_code == 'I4'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'I4 Proposition Set';"""
        assert I4PropositionSet.crm_label == 'I4 Proposition Set'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Checks that I4 is an abstract entity;"""
        assert ABC in I4PropositionSet.__bases__

    # ------------------------- #

    def test_inherits_from_e73(self) -> None:
        """Checks that I4 inherits from E73 Information Object;"""
        assert issubclass(I4PropositionSet, E73InformationObject)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Checks that I4 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(I4PropositionSet, E1CRMEntity)
