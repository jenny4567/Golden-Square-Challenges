from lib.count_words import *
import pytest

def test_cw_is_string():
    with pytest.raises(Exception) as e:
        result = count_words(12)
    error_message = str(e.value)
    assert error_message == "Not a string!"

def test_correct_count():
    result = count_words("hello")
    assert result == 'Number of words: 1'

def test_multiply_words():
    result = count_words("hello my name is emma")
    assert result == 'Number of words: 5'

def test_special_chars():
    result = count_words("I can't think of anything to say thank-you, good-bye")
    assert result == 'Number of words: 9'