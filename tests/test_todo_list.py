from lib.todo_list import *

def test_todo_list_init():
    my_list = TodoList()
    assert my_list.tasks == []