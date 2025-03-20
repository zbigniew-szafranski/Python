### 🔴 Niezbędnik 

# Składnia wywołania funkcji:  nazwa_funkcji ( argumenty )
text = "NAPIS mój napis napis"
print(text)
print(len(text))  # ==> 21

# Składnia wywołania metody:  obiekt . nazwa_metody ( argumenty )
print(text.count("napis"))  # ==> 2

# Niektóre operacje robimy funkcjami, a niektóre metodami, nie ma ogólnej zasady kiedy która opcja. Python jest pod tym względem niespójny. Musisz jednak pamiętać, co jest funkcją, a co metodą, bo nie można ich mieszać.

# ❌ Nie możesz użyć metody jak funkcji
# count(text, "napis")  # ==> NameError: name 'count' is not defined  

# ❌ Nie możesz użyć funkcji jak metody
# text.len()  # ==> AttributeError: 'str' object has no attribute 'len' 

# Hint: Użyj Ctrl+Space po kropce, aby wyświetlić pop-up z podpowiedziami.
# text.

# Pora na podobieństwa. Metody są wciąż dosyć podobne do funkcji - obowiązują te same zasady przekazywania argumentów, jak i zwracania wartości.

# Różne typy obiektów mają dostępne różne metody, np. na string'ach można wywołać .count(), .upper(), .lower() i inne. Z kolei int'y mają zupełnie inny zestaw metod.
number = 2
# text.
# number.

# Metoda .upper() zwraca nowy taki sam string, z tym że wszystkie litery są wielkie.
text = "NAPIS mój napis napis"
print('wielkimi literami: ', text.upper())
print('małymi literami:   ', text.lower())
print('oryginalny tekst:  ', text)

### 🔴 Ćwiczenie: 

# Napisz program, który pyta użytkownika jak się nazywa, a następnie generuje dla niego username (nazwę użytkownika) małymi literami i nie zawierający spacji. 
# 1. Jeśli użytkownik przedstawi się wieloma słowami (np. imieniem i nazwiskiem), wówczas spacje należy ZASTĄPIĆ podkreśleniami. Na przykład, przedstawiam się jako "Jan Kowalski" i generowany jest username jan_kowalski. 
# 2. Do zamiany spacji na podkreślenia musisz użyć metody, która NIE została przedstawiona w tej lekcji - Twoim zadaniem jest wyszukać ją korzystając z Ctrl+Space.

