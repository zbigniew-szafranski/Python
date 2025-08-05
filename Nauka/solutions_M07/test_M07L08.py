from M07L08_pp import find_next_id, add_todo, TodoItem, read_db_or_exit, save_db, DB_FILENAME

def test_empty_list():
    todos = []
    got = find_next_id(todos)
    assert got == 1


def test_single_todoitem_with_id_equals_one():
    todos = [TodoItem(id=1, description='', done=False)]
    got = find_next_id(todos)
    assert got == 2

def test_single_todoitem_with_id_equals_two():
    todos = [TodoItem(id=2, description='', done=False)]
    got = find_next_id(todos)
    assert got == 1

def test_multiple_todoitems():
    todos = [
        TodoItem(id=4, description='', done=False),
        TodoItem(id=2, description='', done=False),
        TodoItem(id=1, description='', done=False),
    ]
    got = find_next_id(todos)
    assert got == 3

def test_add_todo():
    todos = [
        TodoItem(id=4, description='', done=False),
        TodoItem(id=2, description='', done=False),
        TodoItem(id=1, description='', done=False),
    ]
    add_todo('desc', todos)
    assert todos == [
        TodoItem(id=4, description='', done=False),
        TodoItem(id=2, description='', done=False),
        TodoItem(id=1, description='', done=False),
        TodoItem(id=3, description='desc', done=False),
    ]

def test_persistence(tmpdir):
    with tmpdir.as_cwd():
        todos = [
            TodoItem(id=4, description='', done=False),
            TodoItem(id=2, description='', done=False),
            TodoItem(id=1, description='', done=False),
        ]
        save_db(todos)
        got = read_db_or_exit()
        assert got == todos