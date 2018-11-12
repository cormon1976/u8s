"""Pytest Generics"""

import pytest

from camogie import app

@pytest.fixture
def fake_app():
    """Return a test app via the test_client method"""
    test_app = app.test_client()
    return test_app