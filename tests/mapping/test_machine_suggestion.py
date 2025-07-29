"""Test the machine suggestion functionality.

Things in the sidebar can be accessed like this: ezmapapp.sidebar[0].root.button
but the file_uploader is not supported in the test object.
"""
from io import BytesIO
from pathlib import Path
from unittest.mock import MagicMock, patch

from streamlit.testing.v1 import AppTest


@patch("streamlit.sidebar.file_uploader")
def test_machine_suggestion(mock_file: MagicMock, ezmapapp: AppTest) -> None:
    """Test the machine suggestion functionality.

    The test object doesn't support file_uploader, see
    https://github.com/streamlit/streamlit/issues/8093#issuecomment-2317330346
    """
    test_data = Path(__file__).parents[2] / "test_files" / "oht67test.csv"
    mock_file.return_value = BytesIO(test_data.read_bytes())
    mock_file.return_value.name = str(test_data)
    assert (
        not ezmapapp.markdown
        or "Classify Rows and Split Data" not in ezmapapp.markdown[-1].value
    )
    ezmapapp.run()
    assert not ezmapapp.exception, "App raised an exception during run."
    assert "Classify Rows and Split Data" in ezmapapp.markdown[-1].value
