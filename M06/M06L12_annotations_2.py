### 🔴 Adnotacje list

# W poprzedniej lekcji dodawaliśmy adnotacje typów takich jak int, RenameOperation czy list.

# W tym ostatnim przypadku jednak tracimy informację, jakiego typu są elementy tej listy.

# Tym razem dodamy tą informację.

# W tym celu skorzystamy z wbudowanego modułu typing, który pozwala na bardziej zaawansowane adnotacje typów:

from typing import List  # z dużej litery!

def print_all(strings: List[str]) -> None:  # tak, używamy List[str] - w nawiasach kwadratowych określamy typ elementów listy
    for s in strings:
        print(s)
        
print_all(['a', 'b', 'c'])

# W Pythonie 3.8 i starszym musimy użyć typing.List zamiast list, ponieważ samo list nie pozwala jeszcze na zapis list[str].

# Jednak od Pythona 3.9 można już stosować zapis list[str].

### 🔴 Ćwiczenie

# Uzupełnij kod z ćwiczenia M06L10 tak, aby użyć adnotacji typów - zarówno prostych, jak i List.