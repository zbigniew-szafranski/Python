import os
import glob
NEW_EXTENSION = '.bak'

class RenameOperation:
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name

    def __str__(self):
        return f"{self.old_name} -> {self.new_name}"

    def __repr__(self):
        return f"RenameOperation(old_name={self.old_name!r}, new_name={self.new_name!r})"

    def execute(self):
        os.rename(self.old_name, self.new_name)

    def __eq__(self, other):
        return self.old_name == other.old_name and self.new_name == other.new_name


def get_filename_and_extension(filename):
    if '.' in filename:
        tokens = filename.rsplit('.', maxsplit=1)
        name, extension = tokens
    else:
        name= filename
        extension = ""
    return [name, extension]


def collect_operation(filename):
    name, extension = get_filename_and_extension(filename)
    new_filename = name + NEW_EXTENSION
    operation = RenameOperation(filename, new_filename)
    return operation


def print_operations(operations):
    print("ZOSTANĄ DOKONANE NASTĘPUJĄCE ZMIANY:")
    for op in operations:
        print(op)


def execute_operations(operations):
    for op in operations:
        op.execute()
        print("Zmieniono", op)


def main():
    pattern = input('Podaj wzorzec: ')
    filenames = glob.glob(pattern)
    operations = [collect_operation(filename) for filename in filenames]

    print_operations(operations)

    choice = input("Czy kontynuować? [t/n] ")
    if choice.lower() == 't':
        execute_operations(operations)
        print("Success!")
    else:
        print("Anulowano!")

if __name__ == "__main__":
    main()