import os
import pytest
import requests
import requests_mock

from pony import orm
from sdk.schema.schema_api import *

db = orm.Database()

sqlite_path = 'D:\\projetos\\domain_reader\\sdk\\db.sqlite3'
if os.path.exists(sqlite_path):
    os.remove(sqlite_path)
db.bind(provider='sqlite', filename='..\\db.sqlite3', create_db=True)
with orm.db_session():
    db.execute('create table tb_usina (id integer primary key autoincrement, nome_longo text);')
    db.execute('insert into tb_usina (nome_longo) values ("angra");')


def test_get_schema():
    # arrange
    app = 'teif'
    solution = 'sager'
    _map = 'usinaDTO'
    schema_api = SchemaApi(db)
    api_response = {
        "model": {"name": "Usina", "table": "tb_usina"},
        "fields": [
            {"name": "nome_longo", "alias": "nome", "type": "str"}
        ],
        "filter": {"name": "byName", "expression": 'nome = :nome'}
    }

    # action
    with requests_mock.Mocker() as m:
        m.get(schema_api._get_schema_api_url(solution, app, _map),
              status_code=200, json=api_response)

        response = schema_api.get_schema(solution, app, _map)

    # assert
    assert len(response) == 1
