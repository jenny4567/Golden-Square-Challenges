from lib.todo import *
import pytest

def test_check_if_string():
    with pytest.raises(Exception) as e: 
        result = task_checker(12)
    error_message = str(e.value)
    assert error_message == "Not a string!"

def test_if_contains_to_do():
    assert task_checker("#TODO washing up") == True

def test_if_doesnt_contain_to_do():
    assert task_checker("washing up") == False

def test_to_do_no_hash():
    assert task_checker("TODO washing up") == False

def test_todo_and_task():
    assert task_checker("#TODO") == False
