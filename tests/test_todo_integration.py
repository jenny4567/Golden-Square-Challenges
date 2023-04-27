from lib.todo2 import *
from lib.todo_list import *
import pytest

def test_add_adds_task():
    todo_list = TodoList()
    walkies = Todo("Walk the dog")
    snack = Todo("Eat some crisps")
    todo_list.add(snack)
    todo_list.add(walkies)
    result = []
    for item in todo_list.tasks:
        result.append(item.task)
    assert result == ["Eat some crisps", "Walk the dog"]

def test_incomplete_tasks():
    todo_list = TodoList()
    walkies = Todo("Walk the dog")
    snack = Todo("Eat some crisps")
    todo_list.add(snack)
    todo_list.add(walkies)
    walkies.mark_complete()
    assert todo_list.incomplete() == ["Eat some crisps"] 

def test_complete_tasks():
    todo_list = TodoList()
    walkies = Todo("Walk the dog")
    snack = Todo("Eat some crisps")
    todo_list.add(snack)
    todo_list.add(walkies)
    walkies.mark_complete()
    assert todo_list.complete() == ["Walk the dog"]     

def test_give_up():
    todo_list = TodoList()
    walkies = Todo("Walk the dog")
    snack = Todo("Eat some crisps")
    todo_list.add(snack)
    todo_list.add(walkies)
    todo_list.give_up()
    assert len(todo_list.incomplete()) == 0