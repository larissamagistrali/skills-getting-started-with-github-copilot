import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset the in-memory activity data between tests."""
    original_state = copy.deepcopy(activities)

    yield

    activities.clear()
    activities.update(copy.deepcopy(original_state))


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def sample_activity():
    return "Chess Club"


@pytest.fixture
def sample_email():
    return "student@example.com"
