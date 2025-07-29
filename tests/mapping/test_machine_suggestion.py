"""Test the machine suggestion functionality.

Things in the sidebar can be accessed like this: ezmapapp.sidebar[0].root.button
but the file_uploader is not supported in the test object.
"""
from pathlib import Path
from unittest.mock import MagicMock, patch

import pandas as pd
from streamlit.testing.v1 import AppTest


# @patch("streamlit.file_uploader")
def test_machine_suggestion(ezmapapp: AppTest) -> None:
    """Test the machine suggestion functionality.

    The test object doesn't support file_uploader, see
    https://github.com/streamlit/streamlit/issues/8093#issuecomment-2317330346
    """
    # test_data = Path(__file__).parent.parent.parent / "test_files" / "oht67test.csv"
    # mock_file.return_value = test_data.read_bytes()
    # assert (
    #     not ezmapapp.markdown
    #     or "Classify Rows and Split Data" not in ezmapapp.markdown[-1]
    # )
    print("\nPre file upload markdown:")
    print("\n".join(">" + str(i) for i in ezmapapp.markdown))
    ezmapapp.run()
    print("\nPost file upload markdown:")
    print("\n".join(">" + str(i) for i in ezmapapp.markdown))

    assert "A tool for mapping" in ezmapapp.markdown[-1]
    assert "Classify Rows and Split Data" in ezmapapp.markdown[-1]
