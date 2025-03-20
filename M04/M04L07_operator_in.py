### 🔴 Kiedy jeszcze przydają się słowniki?

# W poprzedniej lekcji słownik służył do reprezentowania pojedynczej osoby - a zatem zbieraliśmy kilka informacji takich jak imię, nazwisko, id czy PESEL i grupowaliśmy je w jedną całość. Słowniki często są wykorzystywane do tego celu, chociaż później poznamy lepszy sposób, jakim są klasy.

# Słowniki służą także do innych celów. Jeżeli chcesz zliczyć liczbę wystąpień danego słowa w tekście, to możesz zrobić to bez słowników:

text = 'ile razy pojawia się słowo ile w tym tekście'
words = text.split()

counter = 0
for word in words:
    if word == 'ile':
        counter += 1
print("Słowo 'ile' pojawia się", counter, 'razy')

# Jednak co, gdy chcesz zliczyć liczbę wystąpień każdego ze słów? Wówczas przyda się słownik, którego kluczami są poszczególne słowa, a wartościami liczba ich wystąpień, np.:

counter = {'ile': 2, 'razy': 1, 'pojawia': 1, 'się': 1, 'słowo': 1, 'w': 1, 'tym': 1, 'tekście': 1}
print('counter =', counter)

# W ćwiczeniu Twoim zadaniem jest skonstruować taki słownik. Oczywiście nie zakładając, jakie konkretnie słowa mogą się pojawić.

# Operator `in` pozwala sprawdzić, czy dany string zawiera podstring lub czy dana lista zawiera dany element:

print('CD' in 'ABCDE')  # ==> True
print('C' in ['A', 'B', 'C'])  # ==> True
print('C' in ['A', 'B', 'CD'])  # ==> False

# W przypadku słowników w ten sposób możesz sprawdzić obecność klucza (ale nie wartości!)

if 'ile' in counter:
    print('już jest')  # ==> już jest
else:
    print('jeszcze nie')
    
if 2 in counter:
    print('dwójka jest')
else:
    print('nie ma dwójki')  # ==> nie ma dwójki
    
# Jeśli nie wiesz, czy dany klucz istnieje, a chcesz pobrać wartość, użyj metody .get():

print(counter.get('ile', 0))  # ==> 2  # zwraca wartość dla klucza 'ile'
print(counter.get('nie-istnieje', 0))  # ==> 0  # zwraca wartość domyślną - to, co jest przekazane jako drugi argument

### 🔴 Ćwiczenie

# 1. Mając podany tekst zlicz poszczególne słowa.
# 2. Wyświetl w tabeli ile razy występuje każde ze słów.
# 3. Nie zwracaj uwagi na wielkość liter w słowach, to znaczy "A" oraz "a" to jest to samo słowo. 
# 4. W jaki jeszcze sposób przetworzył(a)byś tekst zanim podzielisz go na słowa?