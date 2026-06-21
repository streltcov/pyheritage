# -*- coding: utf-8 -*-

"""Tests for D3 Formal Derivation;

"""

# pylint: disable=E0401,C0116,W0612

from tests.cidoc.crmdig.helpers import make_e7_kwargs

from pyheritage.cidoc.crmdig.entities import (
    D3FormalDerivation,
    D10SoftwareExecution,
)
from pyheritage.cidoc.crmdig.properties import (
    L21UsedAsDerivationSource,
    L22CreatedDerivative,
)


class TestD3FormalDerivation:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D3';"""
        assert D3FormalDerivation.crm_code == 'D3'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D3 Formal Derivation';"""
        assert D3FormalDerivation.crm_label == 'D3 Formal Derivation'

    # ------------------------- #

    def test_inherits_from_d10(self) -> None:
        """Verify D3 inherits from D10 Software Execution;"""
        assert issubclass(D3FormalDerivation, D10SoftwareExecution)

    # ------------------------- #

    def test_mro_includes_l21(self) -> None:
        """Verify L21 (used as derivation source) mixin is in D3 MRO;"""
        assert L21UsedAsDerivationSource in D3FormalDerivation.__mro__

    # ------------------------- #

    def test_mro_includes_l22(self) -> None:
        """Verify L22 (created derivative) mixin is in D3 MRO;"""
        assert L22CreatedDerivative in D3FormalDerivation.__mro__

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D3 can be instantiated with required kwargs;"""
        obj = D3FormalDerivation(**make_e7_kwargs('D3'))
        assert obj.id is not None
