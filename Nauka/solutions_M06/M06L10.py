### 🔴 Ćwiczenie

# Napisz program służący do zarządzania listą zadań do wykonania (todolist).

# Program powinien wczytać listę zadań z pliku CSV takiego jak todos.csv, a następnie wyświetlić wszystkie zadania w tabeli, a także podsumowanie ile zadań jest już wykonanych.

# Każde zadanie składa się z id, opisu oraz informacji, czy zadanie zostało już wykonane (znak 'x'), czy jeszcze nie (znak '-').

import csv

PATH = "M06/todos.csv"
FIELDNAMES = "ID DONE? DESCRIPTION"
UNDERLINE = "-- ---- --------------"
COUNT_OF_TASKS = "Liczba wykonanych zadań:"

class Task:
    def __init__(self, row):
        self.id = row["id"]
        self.description = row['desc']
        self.status = row['done']

    def __str__(self):
        return f"{self.id:>3} {self.status:^3} {self.description}"

    def __repr__(self):
        return f"Task(id={self.id!r}, description={self.description!r}, status={self.status!r})"


def count_done(tasks):
    return len([t for t in tasks if t.status == 'x'])

def count_tasks(tasks):
    return len(tasks)


def download_tasks(filename):
    with open(filename) as stream:
        reader = csv.DictReader(stream)
        tasks = [Task(row) for row in reader]
        return tasks

def main():
    tasks_list = download_tasks(PATH)
    print(FIELDNAMES)
    print(UNDERLINE)
    for task in tasks_list:
        print(task)
    print(COUNT_OF_TASKS, f"{count_done(tasks_list)}/{count_tasks(tasks_list)}")

if __name__ == "__main__":
    main()


