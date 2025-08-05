### 🔴 Ćwiczenie

# Rozwiń program z poprzedniego ćwiczenia tak, aby znajdować wszystkie pliki pasujące do podanego przez użytkownika wzorca i zmienić ich rozszerzenie na .bak.
# Na ten moment dalej jedynie wyświetl, jaką zmianę byś dokonał(a) - realną zmianą nazwy pliku zajmiemy się w kolejnych lekcjach.
# import os
import glob
NEW_EXTENSION = '.bak'
pattern = input('Podaj wzorzec: ')
filenames = glob.glob(pattern)
print("Zostaną dokonane następujące zmiany:")
for  filename in filenames:
        if '.' in filename:
            tokens = filename.rsplit('.', maxsplit=1)
            name = tokens[0]
            extension = tokens[1]
        new_filename = name + NEW_EXTENSION
        print(filename, '->', new_filename)
        # os.rename(filename, new_filename)
        # print(f"Zmieniono rozszerzenie: {filename} → {new_filename}")

