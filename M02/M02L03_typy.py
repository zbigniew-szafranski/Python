### Typy, klasy, obiekty, wartości, zmienne - o co chodzi?

### 🔴 Niezbędnik

# W Pythonie OBIEKTEM (= wartość) jest każda dana. Poniżej obiektem jest "napis-obiekt".
# Z kolei variable to ZMIENNA. Zmienne nie są obiektami - zmienne WSKAZUJĄ na obiekty (więcej o tym w jednej z kolejnych lekcji).
variable = "napis-obiekt"

# W Pythonie każdy OBIEKT ma TYP (= jest pewnej KLASY).
print(type("tekst"))  # ==> <class 'str'>  # string / napis
print(type(2))        # ==> <class 'int'>  # integer / liczba całkowita
print(type(2.0))      # ==> <class 'float'>  # float / liczba zmiennoprzecinkowa (całkowita lub nie)

# To tak jak na biurku możesz mieć różnego TYPU OBIEKTY - kartki czy długopisy.
# Możesz mieć wiele obiektów jednego typu - wiele kartek, ale wszystkie są kartkami.

# Typ obiektu robi dużą różnicę. Na każdym typie obiektów można wykonywać inne operacje. Na przykład, dwa integer'y można podzielić przez siebie, ale nie można podzielić dwóch stringów.
print(10 / 5)  # ==> 2.0
print("asdf" / "qwer")  # ==> TypeError: unsupported operand type(s) for /: 'str' and 'str'
print("10" / "5")  # ==> TypeError: unsupported operand type(s) for /: 'str' and 'str'

# Niektóre operacje (operator plusa) można wykonywać na obiektach różnych typów, ale sposób działania jest zupełnie inny - dodanie dwóch liczb sumuje je, ale dodanie dwóch stringów skleja je (tzw. konkatenacja).
first = 10
second = 5
print(first + second)  # ==> 15

first = "10"
second = "5"
print(first + second)  # ==> 105

# Czasami konieczne są KONWERSJE typów. Np. funkcja input zwraca zawsze obiekty typu string, nawet jeśli użytkownik wprowadził liczbę. Do konwersji służą wbudowane funkcje str, int, float i inne.
# first = input("Podaj liczbę: ")
first = "123"
first_number = int(first)  # wbudowana funkcja int ZWRACA nowego int'a na podstawie string'a (wcale NIE ZMIENIA string'a w int'a)
print(type(first_number))  # ==> <class 'int'>
print(type(first))  # ==> <class 'str'>  # obiekt pod zmienną first nie zmienił swojego typu!

# Zmienne nie mają typów, bo zmienne to NIE są obiekty - zmienne jedynie wskazują na obiekty, a to obiekty mają typy. Więcej o tym w jednej z kolejnych lekcji.

### 🔴 Ćwiczenie

# Napisz kalkulator, który pyta o dwie liczby i wylicza ich sumę.
# Twój kalkulator nie musi być odporny na podanie czegoś innego niż liczby.