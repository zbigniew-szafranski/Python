import os

old_name = input('Podaj nazwę plik do zmiany: ')
new_name = input("Podaj nową nazwę pliku: ")

os.rename(old_name, new_name)
print(f"Zmieniono nazwę: {old_name} → {new_name}")
