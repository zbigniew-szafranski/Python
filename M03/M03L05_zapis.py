### 🔴 Jak zapisać plik?

content = 'ten tekst chcemy umieścić w pliku'
writer = open('nowy.txt', 'w')  # jeśli plik istnieje, to zostanie nadpisany!!!
writer.write(content)  # uwaga - write w przeciwieństwie do print'a nie dodaje znaku nowej linii!
writer.write('możesz zapisać więcej tekstu\n')
writer.write('to będzie w kolejne linii dzięki \\n')
writer.close()
# po zamknięciu strumienia mamy już gwarancję, że wszystko dotarło na dysk
print(':-) Sukces')

# A jak to zrobić z with'em?

content = 'ten tekst chcemy umieścić w pliku'
with open('nowy2.txt', 'w') as writer:
    writer.write(content)
    writer.write('możesz zapisać więcej tekstu\n')
    writer.write('to będzie w kolejne linii dzięki \\n')
    # implicit writer.close() - daje nam to gwarancję, że faktycznie zmiany dotrą na dysk
print(':-) Sukces')    

### 🔴 Ćwiczenie

# 1. Rozwiń program z poprzedniego ćwiczenia tak, aby zapisać zanonimizowany tekst do nowego wyjściowego pliku. 
# 2. Poproś użytkownika zarówno o nazwę pliku wejściowego (tego, który mamy odczytać, np. plik.txt), jak i wyjściowego (tego, do którego mamy zapisać). 
# 3. Jeżeli użytkownik nie poda nazwy pliku wyjściowego, wówczas wypisz zanominimizowany tekst funkcją print.
# 4. Jeżeli plik wyjściowy już istnieje, to go nie nadpisuj. W tym celu trzeba wykorzystać funkcję open w inny sposób. Jak? Znajdź w dokumentacji tej funkcji!