"""Test fixtures etc."""
import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture(scope="function")
def ezmapapp() -> AppTest:
    """Provide a basic app. instance for testing."""
    return AppTest.from_file("ezmapper.py", default_timeout=60)
