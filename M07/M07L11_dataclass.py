### 🔴 dataclass'y - szybki sposób na tworzenie klas

# Często Twoje klasy wymagają metod takich jak:

# - __init__
# - __repr__ (dla łatwiejszego debugowania)
# - __eq__ (dla testów)

# Ale te metody są bardzo schematyczne:

class Expense:
    def __init__(self, amount: int, description: str):
        self.amount = amount
        self.description = description
        print(f'Sukces! {self.amount}')
        
    def __eq__(self, other):
        return self.amount == other.amount and self.description == other.description
    
    def __repr__(self):
        return f"Expense(amount={self.amount!r}, description={self.description!r})"

e = Expense(2.5, 'Ziemniaki')
e2 = Expense(2.5, 'Ziemniaki')
print(e)
print(e == e2)
    
# Dlatego wymyślono mechanizm dataclass, który powoduje automatyczne wygenerowanie m.in. tych trzech metod. Wystarczy tylko określić jakie pola będzie mieć klasa:

from dataclasses import dataclass

@dataclass
class Expense:
    amount: int
    description: str
        
    # Jeśli jest potrzeba wykonania czegoś nietypowego w __init__, wówczas piszemy __post_init__ zamiast __init__:
    def __post_init__(self):
        print(f'Sukces! {self.amount}')
        
e = Expense(2.5, 'Ziemniaki')
e2 = Expense(2.5, 'Ziemniaki')
print(e)
print(e == e2)

### 🔴 Ćwiczenie

# Przepisz kod z poprzedniego ćwiczenia tak, aby klasę TodoItem zaimplementować jako dataclass.