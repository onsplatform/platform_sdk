import mock
from pony import orm
from platform_sdk.reader.orm_map import RemoteField, RemoteMap


def test_remote_field_optional_build():
    # arrange
    remote_field = RemoteField('nome', str, 'nome_longo', False)

    # action
    ret = remote_field.build()

    # assert
    assert isinstance(ret, orm.Optional)
    assert ret.column == 'nome_longo'
    assert ret.py_type == str

def test_remote_field_required_build():
    # arrange
    remote_field = RemoteField('nome', str, 'nome_longo', True)

    # action
    ret = remote_field.build()

    # assert
    assert isinstance(ret, orm.Required)
    assert ret.column == 'nome_longo'
    assert ret.py_type == str

def test_remote_field():
    # arrange
    remote_field = RemoteField('nome', str, 'nome_longo', False)

    # assert
    assert remote_field.name == 'nome'
    assert remote_field.column == 'nome_longo'
    assert remote_field.field_type == str
    assert remote_field.required == False


def test_remote_map():
    # arrange
    remote_field = RemoteField('nome', str, 'nome_longo')
    remote_map = RemoteMap('Usina', 'tb_usina', [remote_field])

    # assert
    assert remote_map.name == 'Usina'
    assert remote_map.table == 'tb_usina'
    assert len(remote_map.fields) == 1

def test_remote_map_build():
    # arrange
    remote_field = RemoteField('nome', str, 'nome_longo')
    remote_map = RemoteMap('Usina', 'tb_usina', [remote_field])

    # action
    ret = remote_map.build(orm.Database())

    # assert
    assert ret.__name__ == 'Usina'
    assert hasattr(ret, 'id')
    assert hasattr(ret, 'nome')
    assert ret._table_ == 'tb_usina'


