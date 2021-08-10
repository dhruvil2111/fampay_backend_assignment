import pytest

from backend_assignment_fampay.users.models import User
from backend_assignment_fampay.users.tests.factories import UserFactory

@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath

@pytest.fixture
def user() -> User:
    return UserFactory()
