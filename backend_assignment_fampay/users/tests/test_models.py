import pytest

from backend_assignment_fampay.users.models import User

pytestmark = pytest.mark.django_db

def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"
