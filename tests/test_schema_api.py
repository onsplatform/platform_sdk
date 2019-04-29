import os
import pytest
import requests
import requests_mock

from pony import orm
from ..schema.schema_api import *

db = orm.Database()

# todo: remove
sqlite_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)), 'db.sqlite3')
if os.path.exists(sqlite_path):
    os.remove(sqlite_path)
db.bind(provider='sqlite', filename='..\\db.sqlite3', create_db=True)
with orm.db_session():
    db.execute(
        'create table tb_usina (id integer primary key autoincrement, nome_longo text, desc text);')
    db.execute(
        'insert into tb_usina (nome_longo, desc) values ("angra 1", "descricao 1");')
    db.execute(
        'insert into tb_usina (nome_longo, desc) values ("angra 2", "descricao 2");')


def test_get_schema():
    # arrange
    app = 'teif'
    solution = 'sager'
    _map = 'usinaDTO'
    schema_api = SchemaApi(db)
    api_response = {
        "model": {"name": "Usina", "table": "tb_usina"},
        "fields": [
            {"name": "nome_longo", "alias": "nome", "type": "str"},
            {"name": "desc", "alias": "descricao", "type": "str"}
        ],
        "filter": {"name": "byName", "expression": 'nome = :nome'}
    }

    # action
    with requests_mock.Mocker() as m:
        m.get(schema_api._get_schema_api_url(solution, app, _map),
              status_code=200, json=api_response)

        response = schema_api.get_schema(solution, app, _map)

    # assert
    assert len(response) == 2
    assert response[0]['nome'] == 'angra 1'
    assert response[1]['nome'] == 'angra 2'
    assert response[0]['descricao'] == 'descricao 1'
    assert response[1]['descricao'] == 'descricao 2'
