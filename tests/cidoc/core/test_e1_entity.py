# -*- coding: utf-8 -*-

"""Tests for E1CRMEntity base model;

"""


# pylint: disable=E0401,C0116,W0612


import re

import pytest
from pydantic import ValidationError

from pyheritage.cidoc.core.entities import E1CRMEntity, E41Appellation, E42Identifier, E55Type


class TestE1CRMEntity:
    """E1 CRM Entity base model tests;

    """

    def test_id_auto_generated(self) -> None:
        """Identity field (@id) test;

        Checks that @id field is automatically generated with UUID format;

        """
        entity = E1CRMEntity()
        assert hasattr(entity, 'id')

        # UUID format check (basic pattern)
        uuid_pattern = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            re.IGNORECASE,
        )
        assert uuid_pattern.match(entity.id)

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Checks that each instance gets a unique @id;"""
        entity1 = E1CRMEntity()
        entity2 = E1CRMEntity()

        assert entity1.id != entity2.id

    # ------------------------- #

    def test_id_serialized_as_at_id(self) -> None:
        """Checks that id field is serialized with @id alias in JSON;"""
        entity = E1CRMEntity()
        json_dict = entity.model_dump(by_alias=True)

        assert '@id' in json_dict
        assert 'id' not in json_dict
        assert json_dict['@id'] == entity.id

    # ------------------------- #

    def test_id_in_json_output(self) -> None:
        """Checks that @id is present in JSON string output;"""
        entity = E1CRMEntity()
        json_str = entity.model_dump_json(by_alias=True)
        assert f'"@id":"{entity.id}"' in json_str

    # === Required CIDOC properties =====

    def test_p1_is_identified_by_field_exists(self) -> None:
        """Checks that P1 is identified by property field exists;"""
        entity = E1CRMEntity()
        assert hasattr(entity, 'p1_is_identified_by')
        assert entity.p1_is_identified_by is None

    # ------------------------- #

    def test_p1_is_identified_by_accepts_appellation(self) -> None:
        """Checks that P1 property accepts E41 Appellation instances;"""
        entity = E1CRMEntity(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Test Name'),
            ],
        )
        assert len(entity.p1_is_identified_by) == 1
        assert isinstance(entity.p1_is_identified_by[0], E41Appellation)

    # ------------------------- #

    def test_p2_has_type_field_exists(self) -> None:
        """Checks that P2 has type property field exists;"""
        entity = E1CRMEntity()
        assert hasattr(entity, 'p2_has_type')
        assert entity.p2_has_type == []

    # ------------------------- #

    def test_p2_has_type_accepts_type(self) -> None:
        """Checks that P2 property accepts E55 Type instances;"""
        entity = E1CRMEntity(
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test Type')]),
            ],
        )
        assert len(entity.p2_has_type) == 1
        assert isinstance(entity.p2_has_type[0], E55Type)

    # ------------------------- #

    def test_p3_has_note_field_exists(self) -> None:
        """Checks that P3 has note property field exists;"""
        entity = E1CRMEntity()
        assert hasattr(entity, 'p3_has_note')
        assert entity.p3_has_note is None

    # ------------------------- #

    def test_p3_has_note_accepts_string(self) -> None:
        """Checks that P3 property accepts string content;"""
        entity = E1CRMEntity(
            p3_has_note=['This is a test note describing the entity',]
        )
        # p3_has_note is coerced to E62String, check the value attribute
        assert entity.p3_has_note is not None
        assert entity.p3_has_note[0].value == 'This is a test note describing the entity'

    # ------------------------- #

    def test_p48_has_preferred_identifier_field_exists(self) -> None:
        """Checks that P48 has preferred identifier property field exists;"""
        entity = E1CRMEntity()
        assert hasattr(entity, 'p48_has_preferred_identifier')
        assert entity.p48_has_preferred_identifier is None

    # ------------------------- #

    def test_p48_has_preferred_identifier_accepts_identifier(self) -> None:
        """Checks that P48 property accepts E42 Identifier instances;"""
        entity = E1CRMEntity(
            p48_has_preferred_identifier=E42Identifier(
                p190_has_symbolic_content='TEST-ID-001',
            ),
        )
        assert entity.p48_has_preferred_identifier is not None
        assert isinstance(entity.p48_has_preferred_identifier, E42Identifier)
        # p190_has_symbolic_content is coerced to E62String, check the value attribute
        assert entity.p48_has_preferred_identifier.p190_has_symbolic_content.value == 'TEST-ID-001'

    # ------------------------- #

    def test_p137_exemplifies_field_exists(self) -> None:
        """Checks that P137 exemplifies property field exists;"""
        entity = E1CRMEntity()
        assert hasattr(entity, 'p137_exemplifies')
        assert entity.p137_exemplifies is None

    # ------------------------- #

    def test_p137_exemplifies_accepts_type(self) -> None:
        """Checks that P137 property accepts E55 Type instances;"""
        entity = E1CRMEntity(
            p137_exemplifies=[E55Type(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Exemplar Type')],
            )],
        )
        assert entity.p137_exemplifies is not None
        assert isinstance(entity.p137_exemplifies[0], E55Type)

    # === Serialization structure =====

    def test_model_dump_includes_all_properties(self) -> None:
        """Checks that model_dump() includes all CIDOC properties in output;"""
        entity = E1CRMEntity(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Entity Name'),
            ],
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Type')]),
            ],
            p3_has_note=['Test note'],
            p48_has_preferred_identifier=E42Identifier(p190_has_symbolic_content='ID-123'),
            p137_exemplifies=[E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Exemplar')])],
        )

        dump = entity.model_dump()

        assert 'p1_is_identified_by' in dump
        assert 'p2_has_type' in dump
        assert 'p3_has_note' in dump
        assert 'p48_has_preferred_identifier' in dump
        assert 'p137_exemplifies' in dump

    # ------------------------- #

    def test_model_dump_by_alias_includes_at_id(self) -> None:
        """Checks that model_dump(by_alias=True) uses @id for identity field;"""
        entity = E1CRMEntity()
        dump = entity.model_dump(by_alias=True)

        assert '@id' in dump
        assert 'id' not in dump

    # ------------------------- #

    def test_json_serialization_structure(self) -> None:
        """Checks JSON serialization structure with all properties;"""
        entity = E1CRMEntity(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Rosetta Stone'),
            ],
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Artifact')]),
            ],
            p3_has_note=['Ancient Egyptian stele'],
            p48_has_preferred_identifier=E42Identifier(p190_has_symbolic_content='EA 24'),
        )

        json_dict = entity.model_dump(by_alias=True, mode='json')

        # Check @id alias
        assert '@id' in json_dict
        assert isinstance(json_dict['@id'], str)

        # Check P1 property structure
        assert 'p1_is_identified_by' in json_dict
        assert isinstance(json_dict['p1_is_identified_by'], list)
        assert len(json_dict['p1_is_identified_by']) == 1
        # E41Appellation serializes with p190_has_symbolic_content as nested E62String
        assert 'p190_has_symbolic_content' in json_dict['p1_is_identified_by'][0]
        assert json_dict['p1_is_identified_by'][0]['p190_has_symbolic_content']['value'] == 'Rosetta Stone'

        # Check P2 property structure
        assert 'p2_has_type' in json_dict
        assert isinstance(json_dict['p2_has_type'], list)
        assert len(json_dict['p2_has_type']) == 1

        # Check P3 property structure (E62String with value field)
        assert 'p3_has_note' in json_dict
        assert json_dict['p3_has_note'][0]['value'] == 'Ancient Egyptian stele'

        # Check P48 property structure
        assert 'p48_has_preferred_identifier' in json_dict
        assert json_dict['p48_has_preferred_identifier']['p190_has_symbolic_content']['value'] == 'EA 24'

        # Check P137 property (None should be excluded in JSON by default)
        assert 'p137_exemplifies' in json_dict
        assert json_dict['p137_exemplifies'] is None

    # ------------------------- #

    def test_json_string_output(self) -> None:
        """Checks complete JSON string output structure;"""
        entity = E1CRMEntity(
            p3_has_note=['Test entity'],
        )

        json_str = entity.model_dump_json(by_alias=True, indent=2)

        assert '@id' in json_str
        assert 'p3_has_note' in json_str
        assert 'Test entity' in json_str

    # ------------------------- #

    def test_nested_entities_serialization(self) -> None:
        """Checks serialization of nested CRM entities;"""
        entity = E1CRMEntity(
            p1_is_identified_by=[
                E41Appellation(
                    p190_has_symbolic_content='Complex Name',
                    p2_has_type=[
                        E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Proper Name')]),
                    ],
                ),
            ],
        )

        dump = entity.model_dump(mode='json')

        # E41Appellation serializes with p190_has_symbolic_content as nested E62String
        assert dump['p1_is_identified_by'][0]['p190_has_symbolic_content']['value'] == 'Complex Name'
        assert len(dump['p1_is_identified_by'][0]['p2_has_type']) == 1

    # ------------------------- #

    def test_crm_code_attribute(self) -> None:
        """Checks that E1CRMEntity has crm_code attribute;"""
        assert hasattr(E1CRMEntity, 'crm_code')

    # ------------------------- #

    def test_p1_accepts_e42_as_identifier(self) -> None:
        """E42 is a subclass of E41 - p1 property should accept it;"""
        entity = E1CRMEntity(
            p1_is_identified_by=[E42Identifier(
                p190_has_symbolic_content='INV-001'
            )]
        )

        assert len(entity.p1_is_identified_by) == 1
        assert isinstance(entity.p1_is_identified_by[0], E42Identifier)
        assert issubclass(type(entity.p1_is_identified_by[0]), E41Appellation)

    # ------------------------- #

    def test_p1_accepts_multiple_appellations(self) -> None:
        """One CRM entity can have multiple names;"""
        entity = E1CRMEntity(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Name 1'),
                E41Appellation(p190_has_symbolic_content='Name 2'),
                E41Appellation(p190_has_symbolic_content='Name 3'),
            ]
        )

        assert len(entity.p1_is_identified_by) == 3

    # ------------------------- #

    def test_p2_accepts_multiple_types(self) -> None:
        """One CRM entity can have multiple types;"""
        entity = E1CRMEntity(
            p1_is_identified_by=[],
            p2_has_type=[
                E55Type(),
                E55Type()
            ]
        )

        assert len(entity.p2_has_type) == 2

    # ------------------------- #

    def test_p1_property_rejects_wrong_range(self) -> None:
        """Checks p1 property - should reject incorrect range value;"""
        with pytest.raises(ValidationError):
            E1CRMEntity(
                p1_is_identified_by=E55Type()
            )

    # ------------------------- #

    def test_extra_fields_not_allowed(self) -> None:
        """Checks that extra fields are not allowed;"""
        with pytest.raises(AttributeError):
            entity = E1CRMEntity(
                custom_field='Custom value',
            )
            assert entity.custom_field == 'Custom value'

    # ------------------------- #

    def test_extra_fields_in_serialization(self) -> None:
        """Checks that extra fields are included in serialization;"""
        with pytest.raises(AssertionError):
            entity = E1CRMEntity(
                p3_has_note=['Base note'],
                extra_property='Extra data',
            )

            dump = entity.model_dump()
            assert 'p3_has_note' in dump
            assert 'extra_property' in dump and dump['extra_property'] == 'Extra data'
