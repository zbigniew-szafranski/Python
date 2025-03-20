### 🔴 Ćwiczenie

# Poniżej widzisz program, który wyświetla pierwszą linię wszystkich plików pasujących do wzorca podanego przez użytkownika.
# Zmodyfikuj ten program tak, aby najpierw wyświetlił listę wszystkich plików, następnie poprosił użytkownika o potwierdzenie, a dopiero potem wyświetlił po jednej linii z każdego z tych plików.

import glob

pattern = input("Podaj pattern: ")
filenames = glob.glob(pattern)
for filename in filenames:
    with open(filename, 'r') as stream:
        content = stream.read()
        lines = content.split('\n')
        first_line = lines[0]
    print(filename, ':', first_line)