import pytest


from ..orms.peewee import Peewee


@pytest.fixture(scope='class')
def db(request):
    create_db = Peewee.db_factory('sqlite', path='wee.db')
    create_db()
    return Peewee
