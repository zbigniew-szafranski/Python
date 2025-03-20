### 🔴 Jak jeszcze prościej otwierać pliki?

# Dotychczasowa wersja
stream = open('plik.txt')
content = stream.read()
stream.close()
print(content)

# Nowa wersja z użyciem tzw. menadżera kontekstu (instrukcja with).
with open('plik.txt') as stream:  # oznacza PRAWIE to samo co stream = open('plik.txt')
    content = stream.read()
    # implicit stream.close()
print(content)

### 🔴 Ćwiczenie

# Popraw kod z poprzedniego ćwiczenia tak, aby użyć instrukcji with.