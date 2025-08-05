from M07L08 import find_next_id, TodoItem


def test_find_next_id():
    assert find_next_id([]) == 1
def test_find_next_id_with_gaps():
    todos = [
        TodoItem(id=1, description='Zadanie pierwsze', done=False),
        TodoItem(id=3, description='Zadanie trzecie', done=True),
        TodoItem(id=4, description='Zadanie czwarte', done=False),
    ]
    assert find_next_id(todos) == 2
def test_find_next_id_sequential():
    todos = [
        TodoItem(id=1, description='Zadanie pierwsze', done=False),
        TodoItem(id=2, description='Zadanie drugie', done=True),
        TodoItem(id=3, description='Zadanie trzecie', done=False),
    ]
    assert find_next_id(todos) == 4