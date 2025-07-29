"""Test fixtures etc."""
from time import sleep

import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture(scope="function")
def ezmapapp() -> AppTest:
    """Provide a basic app. instance for testing."""
    at = AppTest.from_file("ezmapper.py", default_timeout=60)
    yield at
    while (
        getattr(at.session_state, "suggestions_thread", False)
        and at.session_state.suggestions_thread.is_alive()
    ):
        print("Waiting for suggestions to complete... Ctrl+C to stop.")
        sleep(5)
