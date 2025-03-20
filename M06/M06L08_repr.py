### 🔴 Metody specjalne __repr__ i __str__

### 🔴 Metoda __str__

# Wywołanie print'a wywołuje pod spodem metodę specjalną __str__. Dzięki temu print działa z obiektem dowolnego typu, niezależnie czy jest to int, list czy Twoja własna klasa RenameOperation.

number = 2
print('number =', number)
print('number.__str__() =', number.__str__())

text = "asdf"
print('text =', text)
print('text.__str__() =', text.__str__())

# Wystarczy więc zaimplementować metodę __str__, aby określić, jak mają być printowane obiekty Twoich klas:

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
    def __str__(self):
        return f"wydatek w kwocie {self.amount} na {self.description}"

e = Expense(6.50, "Ziemniaki")
print('e =', e)
print('e.__str__() =', e.__str__())

# Co ciekawe, nawet jak nie zdefiniujesz metody __str__, wówczas Python i tak doda taką metodę do Twojej klasy:

class DummyExpense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc

de = DummyExpense(6.50, "Ziemniaki")
print('de =', de)
print('de.__str__() =', de.__str__())
      
### 🔴 Metoda __repr__    
    
# Oprócz metody __str__() mamy jeszcze drugą metodę specjalną __repr__(), która również konwertuje obiekt na napis.

# __str__ powinien zwrócić wersję "dla człowieka", natomiast __repr__ najlepiej, aby zwrócił kod, który nam wygeneruje ten obiekt z powrotem.

# W przypadków liczb rezultat jest taki sam:

number = 10
print(number, number.__str__(), number.__repr__())

# Ale już w przypadku stringów widać różnicę:
text = "asdf"
print(text, text.__str__(), text.__repr__())

# W print oraz w string interpolation domyślnie używana jest metoda __str__. Jeśli jednak chcemy, możemy użyć __repr__:

msg = f"text = {text!r}"
print(msg)

# Zobaczmy jak możemy dodać metodę __repr__ w naszych własnych klasach

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
    def __str__(self):
        return f"wydatek w kwocie {self.amount} na {self.description}"

    def __repr__(self):
        return f"Expense({self.amount!r}, {self.description!r})"  # konieczne !r, aby Python sam otoczył string cudzysłowami!
    
    
e = Expense(6.50, "Ziemniaki")
print('e =', e)
print('e.__str__() =', e.__str__())
print('e.__repr__() =', e.__repr__())

# Warto jeszcze zwrócić uwagę, że kiedy printujemy listę, to uruchamiana jest jej metoda __str__. Jednak dla każdego jej elementu wywołuje już metodę __repr__:

list_ = [1, "asdf", e]
print('list_ =', list_)

### 🔴 Funkcje str() i repr()

# Praktycznie nigdy nie wywołujemy bezpośrednio metod __str__() i __repr__. Zamiast tego wywołujemy funkcje str() i repr(), które dopiero delegują do odpowiednich metod.

print('e =', e)
print('str(e) =', str(e))
print('repr(e) =', repr(e))

### 🔴 Ćwiczenie

# W poprzednim ćwiczeniu zaimplementuj metodę __repr__ oraz __str__ w klasie RenameOperation i wykorzystaj ją w reszcie kodu. 

# Zauważ, że nie będziemy już potrzebowali metody display().

# Jeśli nie wywołujesz nigdzie metody __repr__, to czy jest sens ją implementować?