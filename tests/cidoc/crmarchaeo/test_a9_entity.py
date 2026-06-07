# -*- coding: utf-8 -*-

"""Tests for A9 Archaeological Excavation;

"""

# pylint: disable=E0401,C0116,W0612

import pytest
from pydantic import ValidationError
from tests.cidoc.crmarchaeo.helpers import make_a9, make_s4_kwargs, make_site

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E27Site,
    E41Appellation,
    E53Place,
)
from pyheritage.cidoc.crmarchaeo.entities import A9ArchaeologicalExcavation
from pyheritage.cidoc.crmarchaeo.properties import AP3Investigated
from pyheritage.cidoc.crmsci.entities import S4Observation


class TestA9ArchaeologicalExcavation:

    def test_crm_code(self) -> None:
        """Verify CRM code is A9;"""
        assert A9ArchaeologicalExcavation.crm_code == 'A9'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label matches A9 Archaeological Excavation;"""
        assert A9ArchaeologicalExcavation.crm_label == 'A9 Archaeological Excavation'

    # ------------------------- #

    def test_inherits_from_s4(self) -> None:
        """Verify A9 inherits from S4 Observation;"""
        assert issubclass(A9ArchaeologicalExcavation, S4Observation)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify A9 inherits from E1 CRM Entity;"""
        assert issubclass(A9ArchaeologicalExcavation, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_ap3(self) -> None:
        """Verify AP3 Investigated mixin is in A9 MRO;"""
        assert AP3Investigated in A9ArchaeologicalExcavation.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify UUID @id is auto-generated on creation;"""
        entity = make_a9()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each instance gets a unique UUID;"""
        a = make_a9()
        b = make_a9()

        assert a.id != b.id

    # ------------------------- #

    def test_ap3_field_exists(self) -> None:
        """Verify ap3_investigated field exists;"""
        entity = make_a9()
        assert hasattr(entity, 'ap3_investigated')

    # ------------------------- #

    def test_ap3_accepts_e27(self) -> None:
        """Verify AP3 accepts E27 Site instances;"""
        site = make_site('Akrotiri, Thera')
        entity = A9ArchaeologicalExcavation(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='West House excavation')],
            **make_s4_kwargs(),
            ap3_investigated=[site],
        )

        assert entity.ap3_investigated is not None
        assert len(entity.ap3_investigated) == 1
        assert isinstance(entity.ap3_investigated[0], E27Site)

    # ------------------------- #

    def test_ap3_rejects_e53_not_e27(self) -> None:
        """Verify AP3 rejects E53 Place (only E27 Site accepted);"""
        with pytest.raises(ValidationError):
            A9ArchaeologicalExcavation(
                ap3_investigated=[E53Place(p157_is_at_rest_relative_to=[])],
                **make_s4_kwargs(),
            )

    # ------------------------- #

    def test_ap3_rejects_invalid_type(self) -> None:
        """Verify AP3 raises ValidationError for non-E27 values;"""
        with pytest.raises(ValidationError):
            A9ArchaeologicalExcavation(
                ap3_investigated=['invalid'],
                **make_s4_kwargs(),
            )

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify A9 can be created with an E41 Appellation;"""
        entity = A9ArchaeologicalExcavation(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Excavation of West House')],
            **make_s4_kwargs(),
            ap3_investigated=[make_site('Site')],
        )

        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Excavation of West House'

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id and AP3 fields;"""
        entity = make_a9()
        data = entity.model_dump()

        assert 'id' in data
        assert 'ap3_investigated' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization with by_alias includes @id;"""
        entity = make_a9('West House excavation')
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'West House' in json_str
