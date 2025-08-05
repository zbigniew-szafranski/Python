### 🔴 Ćwiczenie

# Napisz i przetestuj funkcję, która otrzymuje listę TodoItem. Każdy z nich ma pole id. Następnie funkcja sprawdza, czy jest już zadanie z id == 1, następnie id == 2 i zwraca pierwszy wolny id. Funkcja ta przyda się później do generowania nowych id.
# Napisz testy!

class TodoItem:
    def __init__(self, id: int, description: str, done: bool):
        self.id = id
        self.description = description
        self.done = done


def find_free_id(todos: list[TodoItem])-> int:
    ids = {todo.id for todo in todos}
    counter = 1
    while counter in ids:
        counter += 1
    return counter
