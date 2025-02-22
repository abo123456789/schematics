# -*- coding: utf-8 -*-
import pytest

from schemv.iteration import atoms, Atom
from schemv.schema import Schema, Field
from schemv.types import StringType, IntType
from schemv.undefined import Undefined


@pytest.fixture
def player_schema():
    schema = Schema('Player',
        Field('id', IntType()),
        Field('first_name', StringType(required=True)),
        Field('last_name', StringType(required=True)))
    return schema

@pytest.fixture
def player_data():
    return {'id': '42', 'first_name': 'Arthur', 'towel': True}


def test_atoms_api_keys_param(player_schema, player_data):
    assert list(atoms(player_schema, player_data, keys=['value'])) == [
        Atom(name=None, field=None, value='42'),
        Atom(name=None, field=None, value='Arthur'),
        Atom(name=None, field=None, value=Undefined)]
    assert list(atoms(player_schema, player_data, keys=['name'])) == [
        Atom(name='id', field=None, value=Undefined),
        Atom(name='first_name', field=None, value=Undefined),
        Atom(name='last_name', field=None, value=Undefined)]
