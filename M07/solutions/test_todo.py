from M07L03 import find_free_id, TodoItem

def test_empty():
    todos = []
    result = find_free_id(todos)
    assert result == 1

def test_one_task():
    todos = [TodoItem(id=1, description='', done=False)]
    result = find_free_id(todos)
    assert result == 2

def test_two_tasks():
    todos = [TodoItem(id=1, description='', done=False),
            TodoItem(id=2, description='', done=False)]
    result = find_free_id(todos)
    assert result == 3

def test_between_tasks():
    todos = [TodoItem(id=1, description='',done=False),
            TodoItem(id=5, description='', done=False),
            TodoItem(id=3, description='', done=False),
            TodoItem(id=4, description='', done=False)]
    result = find_free_id(todos)
    assert result == 2
