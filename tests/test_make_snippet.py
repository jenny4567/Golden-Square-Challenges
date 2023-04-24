from lib.make_snippet import *
import pytest

def test_make_snippet_from_long():
    result = snippet_maker("This is a long string to be shortened.")
    assert result == "This is a long string..."

def test_make_snippet_from_short():
    result = snippet_maker("Short string")
    assert result == "Short string"

def test_snippet_is_string():
    with pytest.raises(Exception) as e:
        result = snippet_maker(12)
    error_message = str(e.value)
    assert error_message == "Not a string!"

def test_snippet_is_empty():
    with pytest.raises(Exception) as e:
        result = snippet_maker("")
    error_message = str(e.value)
    assert error_message == "Empty string!"