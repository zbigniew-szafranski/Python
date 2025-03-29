### 🔴 Ćwiczenie

# Popraw kod z M03L12 tak, aby wykorzystać unpacking.

# Podpowiedź: w Twoim programie wykorzystujesz metodę `split()`, aby podzielić nazwę pliku na dwie części: nazwę i rozszerzenie. Przypisz te dwie informacje do dwóch osobnych zmiennych w JEDNEJ linii.

import glob
NEW_EXTENSION = '.bak'
pattern = input('Podaj wzorzec: ')
filenames = glob.glob(pattern)
for  filename in filenames:
        if '.' in filename:
            name, extension = filename.rsplit('.', maxsplit=1)
        new_filename = name + NEW_EXTENSION
        print(filename, '->', new_filename)
        # os.rename(filename, new_filename)
        print(f"Zmieniono rozszerzenie: {filename} → {new_filename}")