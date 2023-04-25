from lib.reading_estimator import *
import pytest

def test_filename_is_string():
    with pytest.raises(Exception) as e:
        result = reading_estimator(12)
    error_message = str(e.value)
    assert error_message == "Filename should be a string."

def test_file_is_textfile():
    with pytest.raises(Exception) as e:
        result = reading_estimator("Just a string")
    error_message = str(e.value)
    assert error_message == "Filename does not correspond to text file." 

def test_file_is_in_folder():
    with pytest.raises(Exception) as e:
        result = reading_estimator("Not in folder.md")
    error_message = str(e.value)
    assert error_message == "Filename does not correspond to file in same folder." 

# def test_filename_is_textfile():
#     assert reading_estimator("test_text_file_long.md") != None

# def test_estimated_reading_time_long():
#     assert reading_estimator("test_text_file_long.md") == "Estimated time: 24 mins"
