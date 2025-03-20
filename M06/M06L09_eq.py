### 🔴 Programowanie obiektowe a testowanie

# Na końcu każdego testu zazwyczaj pojawi się instrukcja assert got == expected.

# Jeśli porównujemy inty, listy lub inne typy wbudowane, wówczas takie porównanie działa tak, jak powinno.

# Jednak co w przypadku obiektów naszych własnych klas?

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
e1 = Expense(6.50, "Ziemniaki")
e2 = Expense(6.50, "Ziemniaki")
print(e1 == e2)  # ==> False

# Domyślnie każdy wydatek jest traktowany jako nierówny innym - nawet, jeśli mają ten sam opis i tą samą kwotę!

# Jak to zmienić? Kod `e1 == e2` jest zamieniany pod spodem na `e1.__eq__(e2)`. Wystarczy zatem zaimplementować metodę specjalną __eq__:

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
    def __eq__(self, other):
        return self.amount == other.amount and self.description == other.description
        
e1 = Expense(6.50, "Ziemniaki")
e2 = Expense(6.50, "Ziemniaki")
print(e1 == e2)  # ==> True

### 🔴 Ćwiczenie

# W poprzednim ćwiczeniu napisz testy funkcji collect_operation. Będzie to wymagało zaimplementowania metody RenameOperation.__eq__.