# -*- coding: utf-8 -*-

"""Tests for A4 Stratigraphic Genesis;

"""

# pylint: disable=E0401,C0116,W0612

from abc import ABC

import pytest
from pydantic import ValidationError
from tests.cidoc.crmarchaeo.helpers import make_a4, make_a8, make_e13_kwargs

from pyheritage.cidoc.core.entities import E1CRMEntity, E41Appellation, E53Place
from pyheritage.cidoc.crmarchaeo.entities import (
    A4StratigraphicGenesis,
    A5StratigraphicModification,
    A8StratigraphicUnit,
)
from pyheritage.cidoc.crmarchaeo.properties import (
    AP7Produced,
    AP9TookMatterFrom,
)
from pyheritage.cidoc.crmsci.entities import (
    S10MaterialSubstantial,
    S17PhysicalGenesis,
)


class TestA4StratigraphicGenesis:

    def test_crm_code(self) -> None:
        """Verify CRM code is A4;"""
        assert A4StratigraphicGenesis.crm_code == 'A4'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label matches A4 Stratigraphic Genesis;"""
        assert A4StratigraphicGenesis.crm_label == 'A4 Stratigraphic Genesis'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify A4 is abstract (ABC in MRO);"""
        assert ABC in A4StratigraphicGenesis.__mro__

    # ------------------------- #

    def test_inherits_from_s17(self) -> None:
        """Verify A4 inherits from S17 Physical Genesis;"""
        assert issubclass(A4StratigraphicGenesis, S17PhysicalGenesis)

    # ------------------------- #

    def test_inherits_from_a5(self) -> None:
        """Verify A4 inherits from A5 Stratigraphic Modification;"""
        assert issubclass(A4StratigraphicGenesis, A5StratigraphicModification)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify A4 inherits from E1 CRM Entity;"""
        assert issubclass(A4StratigraphicGenesis, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_ap7(self) -> None:
        """Verify AP7 Produced mixin is in A4 MRO;"""
        assert AP7Produced in A4StratigraphicGenesis.__mro__

    # ------------------------- #

    def test_mro_includes_ap9(self) -> None:
        """Verify AP9 Took Matter From mixin is in A4 MRO;"""
        assert AP9TookMatterFrom in A4StratigraphicGenesis.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify UUID @id is auto-generated on creation;"""
        entity = make_a4()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each instance gets a unique UUID;"""
        a = make_a4()
        b = make_a4()

        assert a.id != b.id

    # ------------------------- #

    def test_ap7_field_exists(self) -> None:
        """Verify ap7_produced field exists with default;"""
        entity = make_a4()

        assert hasattr(entity, 'ap7_produced')
        assert entity.ap7_produced is not None

    # ------------------------- #

    def test_ap7_accepts_a8(self) -> None:
        """Verify AP7 accepts A8 Stratigraphic Unit instances;"""
        su = make_a8('Produced SU')
        entity = A4StratigraphicGenesis(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test A4')],
            **make_e13_kwargs(),
            o18_altered=[make_a8()],
            o17_generated=[make_a8()],
            ap7_produced=[su],
        )

        assert entity.ap7_produced is not None
        assert len(entity.ap7_produced) == 1
        assert isinstance(entity.ap7_produced[0], A8StratigraphicUnit)

    # ------------------------- #

    def test_ap7_rejects_invalid_type(self) -> None:
        """Verify AP7 raises ValidationError for non-A8 values;"""
        with pytest.raises(ValidationError):
            A4StratigraphicGenesis(
                ap7_produced=['invalid'],
                **make_e13_kwargs(),
                o18_altered=[make_a8()],
                o17_generated=[make_a8()],
            )

    # ------------------------- #

    def test_ap7_rejects_empty_list(self) -> None:
        """Verify AP7 raises ValidationError for empty list (min_length=1);"""
        with pytest.raises(ValidationError):
            A4StratigraphicGenesis(
                ap7_produced=[],
                **make_e13_kwargs(),
                o18_altered=[make_a8()],
                o17_generated=[make_a8()],
            )

    # ------------------------- #

    def test_ap9_field_exists(self) -> None:
        """Verify ap9_took_matter_from field exists with default;"""
        entity = make_a4()

        assert hasattr(entity, 'ap9_took_matter_from')
        assert entity.ap9_took_matter_from is not None

    # ------------------------- #

    def test_ap9_accepts_s10(self) -> None:
        """Verify AP9 accepts S10 Material Substantial instances;"""
        source = S10MaterialSubstantial(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Magma source')],
            o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
        )
        entity = A4StratigraphicGenesis(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test A4')],
            **make_e13_kwargs(),
            o18_altered=[make_a8()],
            o17_generated=[make_a8()],
            ap9_took_matter_from=[source],
        )

        assert entity.ap9_took_matter_from is not None
        assert len(entity.ap9_took_matter_from) == 1
        assert isinstance(entity.ap9_took_matter_from[0], S10MaterialSubstantial)

    # ------------------------- #

    def test_ap9_rejects_invalid_type(self) -> None:
        """Verify AP9 raises ValidationError for non-S10 values;"""
        with pytest.raises(ValidationError):
            A4StratigraphicGenesis(
                ap9_took_matter_from=['invalid'],
                **make_e13_kwargs(),
                o18_altered=[make_a8()],
                o17_generated=[make_a8()],
            )

    # ------------------------- #

    def test_ap9_rejects_empty_list(self) -> None:
        """Verify AP9 raises ValidationError for empty list (min_length=1);"""
        with pytest.raises(ValidationError):
            A4StratigraphicGenesis(
                ap9_took_matter_from=[],
                **make_e13_kwargs(),
                o18_altered=[make_a8()],
                o17_generated=[make_a8()],
            )

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes AP7 and AP9 fields;"""
        entity = make_a4()
        data = entity.model_dump()

        assert 'ap7_produced' in data
        assert 'ap9_took_matter_from' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization with by_alias includes @id;"""
        entity = make_a4('Pumice deposition')
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'Pumice deposition' in json_str
