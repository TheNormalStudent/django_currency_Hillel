import pytest
from django.core.management import call_command

@pytest.fixture(autouse=True, scope='function')
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """

@pytest.fixture(autouse=True, scope='session')
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'app/tests/fixtures/sources.json')