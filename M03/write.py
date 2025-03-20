# 1. Rozwiń program z poprzedniego ćwiczenia tak, aby zapisać zanonimizowany tekst do nowego wyjściowego pliku. 
# 2. Poproś użytkownika zarówno o nazwę pliku wejściowego (tego, który mamy odczytać, np. plik.txt), jak i wyjściowego (tego, do którego mamy zapisać). 
# 3. Jeżeli użytkownik nie poda nazwy pliku wyjściowego, wówczas wypisz zanominimizowany tekst funkcją print.
# 4. Jeżeli plik wyjściowy już istnieje, to go nie nadpisuj. W tym celu trzeba wykorzystać funkcję open w inny sposób. Jak? Znajdź w dokumentacji tej funkcji!

file_open = input("Podaj nazwę pliku wejściowego: ")
file_write = input("Podaj nazwę pliku wyjściowego: ")

with open(file_open) as stream:
    content = stream.read()

for digit in '0123456789':
    content = content.replace(digit,'X')

if file_write:
    with open(file_write, 'x') as writer:
        writer.write(content)
    print("Zapisano do pliku")
else:
    print(content)