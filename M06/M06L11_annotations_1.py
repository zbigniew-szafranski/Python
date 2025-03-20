### 🔴 Adnotacje typów

# Wiesz już, że warto umieszczać w kodzie dokumentację w postaci docstringów.

# Można tam umieścić także informacje o typie poszczególnych parametrów jak i wartości zwracanej.

# Jest jednak na to lepszy sposób, dzięki któremu VSCode i inne IDE będą potrafiły wykorzystać tą informację, aby lepiej podpowiadać. Łatwiej będzie ją też znaleźć ludziom.

# Są to adnotacje typów parametrów oraz wartości zwracanej. Można ich używać w sygnaturach funkcji, jak i metod (także metod specjalnych).

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 4))
print(add('asdf', 'qwer'))  # Zwróć uwagę, że adnotacje typów to jedynie adnotacje. Python nie sprawdza, czy faktycznie ma do czynienia z właściwym typem - ani na etapie kompilacji, ani w runtimie.

### 🔴 Ćwiczenie

# Dodaj adnotacje typów w M06L09.