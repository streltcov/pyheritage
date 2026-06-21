# -*- coding: utf-8 -*-

"""Tests for D7 Digital Machine Event;

D7 is declared with ABC — tested for metadata and MRO only;

"""

# pylint: disable=E0401,C0116,W0612

from abc import ABC

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E11Modification,
    E65Creation,
)
from pyheritage.cidoc.crmdig.entities import D7DigitalMachineEvent
from pyheritage.cidoc.crmdig.properties import (
    L10HadInput,
    L11HadOutput,
    L12HappenedOnDevice,
    L18HasModified,
    L23UsedSoftwareOrFirmware,
)


class TestD7DigitalMachineEvent:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D7';"""
        assert D7DigitalMachineEvent.crm_code == 'D7'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D7 Digital Machine Event';"""
        assert D7DigitalMachineEvent.crm_label == 'D7 Digital Machine Event'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify D7 is declared as abstract (ABC);"""
        assert ABC in D7DigitalMachineEvent.__mro__

    # ------------------------- #

    def test_inherits_from_e11(self) -> None:
        """Verify D7 inherits from E11 Modification;"""
        assert issubclass(D7DigitalMachineEvent, E11Modification)

    # ------------------------- #

    def test_inherits_from_e65(self) -> None:
        """Verify D7 inherits from E65 Creation;"""
        assert issubclass(D7DigitalMachineEvent, E65Creation)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify D7 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(D7DigitalMachineEvent, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_l10(self) -> None:
        """Verify L10 (had input) mixin is in D7 MRO;"""
        assert L10HadInput in D7DigitalMachineEvent.__mro__

    # ------------------------- #

    def test_mro_includes_l11(self) -> None:
        """Verify L11 (had output) mixin is in D7 MRO;"""
        assert L11HadOutput in D7DigitalMachineEvent.__mro__

    # ------------------------- #

    def test_mro_includes_l12(self) -> None:
        """Verify L12 (happened on device) mixin is in D7 MRO;"""
        assert L12HappenedOnDevice in D7DigitalMachineEvent.__mro__

    # ------------------------- #

    def test_mro_includes_l18(self) -> None:
        """Verify L18 (has modified) mixin is in D7 MRO;"""
        assert L18HasModified in D7DigitalMachineEvent.__mro__

    # ------------------------- #

    def test_mro_includes_l23(self) -> None:
        """Verify L23 (used software or firmware) mixin is in D7 MRO;"""
        assert L23UsedSoftwareOrFirmware in D7DigitalMachineEvent.__mro__
