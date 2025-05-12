from M07L03 import find_free_id, TodoItem

def test_empty():
    todo_items = []
    result = find_free_id(todo_items)
    assert result == 1

def test_one_task():
    todo_items = [TodoItem(id=1, title="one")]
    result = find_free_id(todo_items)
    assert result == 2

def test_two_tasks():
    todo_items = [TodoItem(id=1, title="one"),
                  TodoItem(id=2, title="two")]
    result = find_free_id(todo_items)
    assert result == 3

def test_between_tasks():
    todo_items = [TodoItem(id=1, title="one"),
                  TodoItem(id=3, title="three"),
                  TodoItem(id=4, title="four")]
    result = find_free_id(todo_items)
    assert result == 2
