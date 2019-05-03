import pytest


from reader.orms.peewee import PeeWee


@pytest.fixture(scope='class')
def db(request):
    create_db = PeeWee.db_factory('sqlite', path='wee.db')
    return create_db()
