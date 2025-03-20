### 🔴 Teoria

# 👉 BŁĄD = WYJĄTEK. Program RZUCIŁ wyjątek = zakończył się błędem.
# 👉 Python ma budowane ponad 100 typów błędów. Można też tworzyć własne. Jednak tylko kilka z nich odpowiada za ponad 90% wszystkich błędów.
# 👉 W przypadku błędu zawsze przewijamy na sam koniec, gdzie pojawia się typ błędu oraz jego komunikat. Dopiero później ewentualnie analizujemy traceback.

### 🔴 Niezbędnik - checklista

# Gdy dostajesz NameError, najprawdopodobniej zrobiłæś literówkę w nazwie zmiennej lub nazwie funkcji.
text = "asdf"
# print(tetx)  # (!)  # ==> NameError: name 'tetx' is not defined
# pirnt(text)  # (!)  # ==> NameError: name 'pirnt' is not defined

# Błędy typu TypeError mówią m.in. o tym, że na danym obiekcie nie da się wykonać danej operacji. Na przykład, nie można użyć funkcji len, aby wyliczyć ile cyfr ma liczba. Możesz za to stworzyć stringa reprezentującego taką samą liczbę i policzyć ile cyfr ma ten string. Często wystarczy dokonać tego typu konwersji typów, jednak często też problem jest bardziej złożony.
print(len("1234"))  # ==> 4  # ok
# print(len(1234))  # ==> TypeError: object of type 'int' has no len()

# Błędy typu ValueError mówią o tym, że co prawda typy są w porządku, ale sama wartość jest niepoprawna. Na przykład, nie każdy string można zamienić na liczbę.
print(int("123"))  # ==> 123  # ok
# print(int("asdf"))  # ==> ValueError: invalid literal for int() with base 10: 'asdf'
# print(int("123.45"))  # ==> ValueError: invalid literal for int() with base 10: '123.45'

# Wszystkie powyższe błędy jak i wiele innych to tzw. błędy WYKONANIA (runtime errors). Pojawiają się one dopiero gdy Python dojdzie do wykonywania konkretnej linii kodu. Dla odmiany błędy KOMPILACJI (compile time errors) pojawiają się zanim w ogóle dojdzie do uruchomienia kodu. Jedynymi błędami tego typu są SyntaxError, IndentationError oraz TabError.
print("SyntaxError to błąd kompilacji, więc ten print w ogóle nie zadziała.")
# invalid_syntax !@#$%^  # ==> SyntaxError: invalid syntax 

# Problem w składni może być wcześniej, niż wskazuje na to traceback.
# print("Kalkulator"
# x = "2"

### 🔴 Ćwiczenie: popraw błędy w poniższych fragmentach kodu.

# = 1 =  
division = 2 / 5
print((division))

# = 2 =
# variable = 1234
# print(Variable)
     
# = 3 =
# x = "asdf"      
# print( type(x)

# = 4 =
# sum_ = 2 + 5
# print[sum_]

# = 5 =
# number = input("Podaj liczbę: ")
# int(number)
# print("Ta liczba ma", len(number), "cyfr.")