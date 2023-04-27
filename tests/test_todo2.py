from lib.todo2 import *
import pytest

def test_todo_initializes():
    walkies = Todo("Walk the dog")
    assert walkies.task == "Walk the dog"
    assert walkies.complete == False

def test_todo_mark_complete():
    walkies = Todo("Walk the dog")
    walkies.mark_complete()
    assert walkies.complete == True  