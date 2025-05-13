import csv
from typing import List, Dict, Any

TODOS_FILENAME = 'M06/todos.csv'

class TodoItem:
    def __init__(self, id: int, description: str, done: bool) -> None:

        self.id = id
        self.description = description
        self.done = done


def create_todo_item_from_dict(row: Dict[str, str]) -> TodoItem:
    return TodoItem(
        id=int(row['id']), # id powinno być int'em a nie stringiem
        description=row['desc'],
        done=(row['done'] == 'x') # done powinno być boolean'em
    )


def read_todos(filename: str) -> List[TodoItem]:
    with open(filename) as stream:
        reader = csv.DictReader(stream)
        todos = [create_todo_item_from_dict(row) for row in reader]
    return todos


def print_todos(todos: List[TodoItem]) -> None:
    print("    ID DONE? DESCRIPTION")
    print("------ ----- -----------")
    for todo in todos:
        if todo.done:
            done = 'x'
        else:
            done = '.'
        print(f"{todo.id:6d} {done:^5} {todo.description}")


def print_summary(todos: List[TodoItem]) -> None:
    done = len([t for t in todos if t.done])
    all_ = len(todos)

    print()
    print(f"Liczba wykonanych zadań: {done}/{all_}")


def main() -> None:
    todos = read_todos(TODOS_FILENAME)
    print_todos(todos)
    print_summary(todos)

if __name__ == "__main__":
    main()
