# -*- coding: utf-8 -*-

"""Tests for D2 Digitization Process;

"""

# pylint: disable=E0401,C0116,W0612

from tests.cidoc.crmdig.helpers import make_s4_kwargs

from pyheritage.cidoc.crmdig.entities import (
    D2DigitizationProcess,
    D11DigitalMeasurementEvent,
)
from pyheritage.cidoc.crmdig.properties import L1Digitized


class TestD2DigitizationProcess:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D2';"""
        assert D2DigitizationProcess.crm_code == 'D2'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D2 Digitization Process';"""
        assert D2DigitizationProcess.crm_label == 'D2 Digitization Process'

    # ------------------------- #

    def test_inherits_from_d11(self) -> None:
        """Verify D2 inherits from D11 Digital Measurement Event;"""
        assert issubclass(D2DigitizationProcess, D11DigitalMeasurementEvent)

    # ------------------------- #

    def test_mro_includes_l1(self) -> None:
        """Verify L1 (digitized) mixin is in D2 MRO;"""
        assert L1Digitized in D2DigitizationProcess.__mro__

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D2 can be instantiated with required kwargs;"""
        obj = D2DigitizationProcess(**make_s4_kwargs('D2'))
        assert obj.id is not None
