# -*- coding: utf-8 -*-

"""Tests for D12 Data Transfer Event;

"""

# pylint: disable=E0401,C0116,W0612

from tests.cidoc.crmdig.helpers import make_e7_kwargs

from pyheritage.cidoc.crmdig.entities import (
    D7DigitalMachineEvent,
    D12DataTransferEvent,
)
from pyheritage.cidoc.crmdig.properties import (
    L14Transferred,
    L15HasSender,
    L16HasReceiver,
)


class TestD12DataTransferEvent:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D12';"""
        assert D12DataTransferEvent.crm_code == 'D12'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D12 Data Transfer Event';"""
        assert D12DataTransferEvent.crm_label == 'D12 Data Transfer Event'

    # ------------------------- #

    def test_inherits_from_d7(self) -> None:
        """Verify D12 inherits from D7 Digital Machine Event;"""
        assert issubclass(D12DataTransferEvent, D7DigitalMachineEvent)

    # ------------------------- #

    def test_mro_includes_l14(self) -> None:
        """Verify L14 (transferred) mixin is in D12 MRO;"""
        assert L14Transferred in D12DataTransferEvent.__mro__

    # ------------------------- #

    def test_mro_includes_l15(self) -> None:
        """Verify L15 (has sender) mixin is in D12 MRO;"""
        assert L15HasSender in D12DataTransferEvent.__mro__

    # ------------------------- #

    def test_mro_includes_l16(self) -> None:
        """Verify L16 (has receiver) mixin is in D12 MRO;"""
        assert L16HasReceiver in D12DataTransferEvent.__mro__

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D12 can be instantiated with required kwargs;"""
        obj = D12DataTransferEvent(**make_e7_kwargs('D12'))
        assert obj.id is not None
