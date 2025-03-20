### 🔴 Metody we własnych klasach

# W poprzedniej lekcji napisaliśmy najprostszą klasę, taką która ma tylko metodę specjalną __init__.

# Teraz pora dodać nową, zwykłą metodę.

# Czegoś takiego nie moglibyśmy zrobić, gdybyśmy reprezentowali wydatek jako słownik. Dzięki zdefiniowaniu własnej klasy jest to jednak możliwe.

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
    def get_amount_as_int(self):
        ''' Return amount in GROSZE as int.  '''
        return int(self.amount * 100)
    
e = Expense(6.50, "Ziemniaki")

print('e.amount =', e.amount)

# Zwróć uwage, że wywołując metodę nie podajesz self'a w nawias okrągłych - bo jego podajesz przed kropką.
grosze = e.get_amount_as_int()

print('Ziemniaki kosztowały', grosze, 'groszy.')

### 🔴 Ćwiczenie

# W poprzednim ćwiczeniu zaimplementuj metodę RenameOperation.display(), która wyświetla operację, jaka zostanie wykonana. Wykorzystaj tę metodę w reszcie kodu.