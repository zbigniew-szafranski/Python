### 🔴 Praca na podlistach - slicing

# Wiesz już, jak uzyskać dostęp do pojedynczego elementu listy:

lista = ['A', 'B', 'C', 'D', 'E']
print('lista[1] =', lista[1])  # ==> 'B'

# Czasami jednak chcesz uzyskać kilka elementów pod rząd. Użyj wówczas składni lista[start:end]:

print('lista[1:3] =', lista[1:3])  # ==> ['B', 'C']

# Zwróć uwagę, że taki zapis zwraca elementy, których index jest co najmniej 1 i MNIEJSZY niż 3. Nie ma zatem elementu, którego index = 3, czyli litery 'D'.

# Możesz pominąć index początkowy, wówczas oznacza to "weź wszystko od początku do wskazanego elementu, bez tego elementu."

print('lista[:3] =', lista[:3])  # ==> ['A', 'B', 'C']

# Możesz pominąć index końcowy, wówczas oznacza to "weź wszystko od wskazanego elementu do końca."

print('lista[1:] =', lista[1:])  # ==> ['B', 'C', 'D', 'E']

# Ta składnia działa także z napisami:

filename = '20210906 notatki.txt'
print('filename[:8] =', filename[:8])  # ==> 20210906

# Możesz używać ujemnych indexów - wówczas liczymy elementy od końca, a nie od początku listy:

print('filename[:-4] =', filename[:-4])  # ==> 20210906 notatki
print('filename[-4:] =', filename[-4:])  # ==> .txt

### 🔴 Ćwiczenie

# Rozwiń program z poprzedniej lekcji tak, aby mógł przyjmować wiele nazw plików. Dla każdego pliku wyświetl ile ma linii, słów i znaków.