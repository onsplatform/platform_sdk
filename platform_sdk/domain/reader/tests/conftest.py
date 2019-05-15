import pytest


from ..orms.peewee import Peewee


@pytest.fixture(scope='class')
def db(request):
    return Peewee
