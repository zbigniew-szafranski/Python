### 🔴 Ćwiczenie

# Popraw kod z ćwiczenia M03L16. W tym ćwiczeniu zmienialiśmy rozszerzenia wielu plików na raz.

# Po pierwsze, zastosuj nowe dobre praktyki, które poznałæś w czwartym i piątym module.

# Po drugie, w tym programie tworzyliśmy listę wszystkich operacji do wykonania. Każdą operację reprezentowaliśmy jako dwuelementowa lista [obecna_nazwa_pliku, nowa_nazwa_pliku].

# Dużo lepiej jest reprezentować operację jako obiekt własnej klasy RenameOperation.

# Stwórz taką klasę i przepisz kod tak, aby ją wykorzystywał.
import os
import glob
NEW_EXTENSION = '.txt'

class RenameOperation:
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name

def change_filenames(pattern):
    operations = []
    filenames = glob.glob(pattern)
    for  filename in filenames:
        if '.' in filename:
            tokens = filename.rsplit('.', maxsplit=1)
            name, extension = tokens
        else:
            name= filename
            extension = ""
        new_filename = name + NEW_EXTENSION
        operations.append(RenameOperation(filename, new_filename))
    return operations


def rename_files(operations, choice):
    if choice.lower() == 't':
        for operation in operations:
            os.rename(operation.old_name, operation.new_name)
            print("Zmieniono:", operation.old_name, "→", operation.new_name)
        print("Success!")
    else:
        print("Anulowano!")

def main():
    pattern = input("Podaj wzorzec: ")
    operations = change_filenames(pattern)

    print("Zostaną dokonane następujące zmiany:")
    for operation in operations:
        print(operation.old_name, "->", operation.new_name)
    choice = input("Czy kontynuować? [t/n] ")
    rename_files(operations, choice)

if __name__ == "__main__":
    main()
