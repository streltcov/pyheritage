# -*- coding: utf-8 -*-

"""Tests for E62String CRM entity;

"""


# pylint: disable=E0401,C0116,W0612


import re

import pytest

from pyheritage.cidoc.core.entities import E59PrimitiveValue, E62String
from pyheritage.cidoc.core.entities._primitives import _coerce_e62  # noqa


class TestE62String:
    """Test E62 String with various string values;

    """

    def test_empty_string(self) -> None:
        """Checks empty string value;"""
        entity = E62String(value='')
        assert entity.value == ''

    # ------------------------- #

    def test_simple_string(self) -> None:
        """Checks simple ASCII string;"""
        entity = E62String(value='Hello World')
        assert entity.value == 'Hello World'

    # ------------------------- #

    def test_long_string(self) -> None:
        """Checks long string value;"""
        long_text = 'A' * 10000
        entity = E62String(value=long_text)
        assert entity.value == long_text
        assert len(entity.value) == 10000

    # ------------------------- #

    @pytest.mark.parametrize("value,description", [
        ('@#$%^&*()', 'symbols'),
        ('_+-=[]{}|', 'programming symbols'),
        (';:,.<>?!', 'punctuation'),
        ('\\/"`~', 'slashes and backticks'),
        ('§¶†‡•‰', 'typographic symbols'),
        ('¢£¥€₽₹', 'currency symbols'),
        ('♠♣♥♦♤♧♡♢', 'card suits'),
        ('★☆✦✧✪✫', 'stars'),
    ])
    def test_string_with_special_chars(self, value: str, description: str) -> None:
        """Checks string with special characters are preserved;"""
        entity = E62String(value=value)
        assert entity.value == value

    # ------------------------- #

    def test_whitespace_only(self) -> None:
        """Checks whitespace-only string;"""
        entity = E62String(value='   ')
        assert entity.value == '   '

    # ------------------------- #

    def test_default_value(self) -> None:
        """Checks default value is empty string;"""
        entity = E62String()
        assert entity.value == ''


# ******************************************************************************************************************* #


class TestE62StringLanguage:
    """Test E62 String language tag validation;

    """

    @pytest.mark.parametrize("language", [
        'en',
        'ru',
        'de',
        'fr',
        'zh',
        'ja',
        'en-US',
        'en-GB',
        'pt-BR',
        'zh-CN',
        'zh-TW',
        'de-CH',
        'sr-Latn-RS',
        'en-GB-oed',
        'ca-ES-valencia',
    ])
    def test_valid_language_tags(self, language: str) -> None:
        """Checks that valid BCP 47 language tags are accepted;"""
        entity = E62String(value='Test', language=language)
        assert entity.language == language

    # ------------------------- #

    @pytest.mark.parametrize("language", [
        'en_US',
        'en.US',
        'en--US',
        '123',
        ' en',
    ])
    def test_invalid_language_tags(self, language: str) -> None:
        """Checks that invalid language tags are rejected;"""
        with pytest.raises(ValueError, match='BCP 47'):
            E62String(value='Test', language=language)

    # ------------------------- #

    def test_language_none_allowed(self) -> None:
        """Checks that None language is allowed;"""
        entity = E62String(value='Test', language=None)
        assert entity.language is None

    # ------------------------- #

    def test_language_default(self) -> None:
        """Checks that default language is None;"""
        entity = E62String(value='Test')
        assert entity.language is None

    # ------------------------- #

    def test_language_case_preserved(self) -> None:
        """Checks that language tag case is preserved;"""
        entity = E62String(value='Test', language='en-US')
        assert entity.language == 'en-US'


# ******************************************************************************************************************* #


class TestE62StringMagicMethods:
    """Test E62 String magic methods;

    """

    def test_str(self) -> None:
        """Checks __str__ returns value;"""
        entity = E62String(value='Hello')
        assert str(entity) == 'Hello'

    # ------------------------- #

    def test_str_empty(self) -> None:
        """Checks __str__ with empty value;"""
        entity = E62String(value='')
        assert str(entity) == ''

    # ------------------------- #

    def test_repr_without_language(self) -> None:
        """Checks __repr__ without language;"""
        entity = E62String(value='Hello')
        assert repr(entity) == "E62('Hello')"

    # ------------------------- #

    def test_repr_with_language(self) -> None:
        """Checks __repr__ with language;"""
        entity = E62String(value='Hello', language='en')
        assert repr(entity) == "E62('Hello', language='en')"

    # ------------------------- #

    def test_repr_unicode(self) -> None:
        """Checks __repr__ with Unicode value;"""
        entity = E62String(value='Hello')
        assert repr(entity) == "E62('Hello')"


# ******************************************************************************************************************* #


class TestE62StringCoercion:
    """Test E62 String coercion function;

    """

    def test_coercion_from_string(self) -> None:
        """Checks coercion from plain string;"""
        entity = _coerce_e62('Hello World')
        assert isinstance(entity, E62String)
        assert entity.value == 'Hello World'

    # ------------------------- #

    def test_coercion_from_dict(self) -> None:
        """Checks coercion from dict;"""
        entity = _coerce_e62({'value': 'Hello', 'language': 'en'})
        assert isinstance(entity, E62String)
        assert entity.value == 'Hello'
        assert entity.language == 'en'

    # ------------------------- #

    def test_coercion_from_dict_no_language(self) -> None:
        """Checks coercion from dict without language;"""
        entity = _coerce_e62({'value': 'Hello'})
        assert isinstance(entity, E62String)
        assert entity.value == 'Hello'
        assert entity.language is None

    # ------------------------- #

    def test_coercion_passthrough(self) -> None:
        """Checks passthrough of existing E62String;"""
        entity = E62String(value='Test')
        assert _coerce_e62(entity) is entity

    # ------------------------- #

    def test_coercion_rejects_non_string(self) -> None:
        """Checks that non-string values are rejected;"""
        with pytest.raises(ValueError, match='Cannot coerce'):
            _coerce_e62(123)  # type: ignore[arg-type]

    # ------------------------- #

    def test_coercion_rejects_list(self) -> None:
        """Checks that list values are rejected;"""
        with pytest.raises(ValueError, match='Cannot coerce'):
            _coerce_e62(['Hello', 'World'])  # type: ignore[arg-type]


# ******************************************************************************************************************* #


class TestE62StringSerialization:
    """Test E62 String serialization;

    """

    def test_model_dump(self) -> None:
        """Checks model_dump output;"""
        entity = E62String(value='Hello', language='en')
        dump = entity.model_dump()

        assert 'value' in dump
        assert dump['value'] == 'Hello'
        assert 'language' in dump
        assert dump['language'] == 'en'

    # ------------------------- #

    def test_model_dump_no_language(self) -> None:
        """Checks model_dump without language;"""
        entity = E62String(value='Hello')
        dump = entity.model_dump()

        assert dump['value'] == 'Hello'
        assert dump['language'] is None

    # ------------------------- #

    def test_model_dump_json(self) -> None:
        """Checks model_dump with mode='json';"""
        entity = E62String(value='Hello World')
        dump = entity.model_dump(mode='json')

        assert dump['value'] == 'Hello World'

    # ------------------------- #

    def test_model_dump_by_alias(self) -> None:
        """Checks model_dump with by_alias=True;"""
        entity = E62String(value='Hello')
        dump = entity.model_dump(by_alias=True)

        assert '@id' in dump
        assert dump['value'] == 'Hello'

    # ------------------------- #

    def test_model_dump_json_string(self) -> None:
        """Checks JSON string output;"""
        entity = E62String(value='Hello')
        json_str = entity.model_dump_json(by_alias=True)

        assert '"@id"' in json_str
        assert '"value"' in json_str
        assert 'Hello' in json_str

    # ------------------------- #

    def test_model_validate(self) -> None:
        """Checks model_validate class method;"""
        entity = E62String.model_validate({'value': 'Test', 'language': 'ru'})

        assert isinstance(entity, E62String)
        assert entity.value == 'Test'
        assert entity.language == 'ru'

    # ------------------------- #

    def test_model_validate_no_language(self) -> None:
        """Checks model_validate without language;"""
        entity = E62String.model_validate({'value': 'Test'})

        assert isinstance(entity, E62String)
        assert entity.value == 'Test'
        assert entity.language is None


# ******************************************************************************************************************* #


class TestE62StringInheritance:
    """Test E62 String inheritance and CRM metadata;

    """

    def test_inherits_from_e59(self) -> None:
        """Checks inheritance from E59PrimitiveValue;"""
        entity = E62String(value='Test')
        assert isinstance(entity, E59PrimitiveValue)

    # ------------------------- #

    def test_crm_code(self) -> None:
        """Checks crm_code attribute;"""
        assert hasattr(E62String, 'crm_code')
        assert E62String.crm_code == 'E62'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Checks crm_label attribute;"""
        assert hasattr(E62String, 'crm_label')
        assert E62String.crm_label == 'E62 String'

    # ------------------------- #

    def test_has_id_field(self) -> None:
        """Checks that @id field exists;"""
        entity = E62String(value='Test')

        assert hasattr(entity, 'id')
        assert entity.id is not None

    # ------------------------- #

    def test_id_is_uuid_format(self) -> None:
        """Checks that id is UUID format;"""
        entity = E62String(value='Test')
        uuid_pattern = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            re.IGNORECASE,
        )

        assert uuid_pattern.match(entity.id)

    # ------------------------- #

    def test_unique_ids(self) -> None:
        """Checks that each instance has unique id;"""
        entity1 = E62String(value='Test')
        entity2 = E62String(value='Test')

        assert entity1.id != entity2.id


# ******************************************************************************************************************* #


class TestE62StringEdgeCases:
    """Test E62 String edge cases;

    """

    def test_null_character(self) -> None:
        """Checks string with null character;"""
        entity = E62String(value='Hello\x00World')
        assert entity.value == 'Hello\x00World'

    # ------------------------- #

    def test_empty_string_with_language(self) -> None:
        """Checks empty string with language tag;"""
        entity = E62String(value='', language='en')

        assert entity.value == ''
        assert entity.language == 'en'
