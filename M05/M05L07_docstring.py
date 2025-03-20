### 🔴 Docstringi

# W Pythonie stringi można tworzyć na co najmniej dwa sposoby:

casual_string = "To musi być w jednej linii"

multiline_string = """
Ten string
Może zawierać
wiele linii!
"""

# Jak w praktyce wykorzystuje się tę drugą opcję? Do pisania DOKUMENTACJI.

# Jak najwięcej informacji staramy się zawrzeć w kodzie, w szczególności w nazwach zmiennych czy funkcji.
# Jednak pewnych informacji nie da się tak zawrzeć - dobrze jest je wtedy spisać w tzw. dokumentacji.
# W Pythonie używamy do tego tzw. docstringa, czyli stringa znajdującego się na samym początku modułu, funkcji lub klasy, tak jak poniżej:

def add(a, b, c, force_conversion=False):
    """Add three numbers.
    
    force_conversion -- forces conversion to float (useful if some numbers may be strings).
    
    """
    
    if force_conversion:
        a = float(a)
        b = float(b)
        c = float(c)
    return a + b + c

# Tak napisana dokumentacja jest rozpoznawana przez Pythona i przez narzędzia.

print(add.__doc__)  # Funkcje (jak i klasy i moduły) mają specjalny atrybut __doc__ przechowujące opis.

# Dokumentację całego modułu umieszczamy na początku całego skryptu, jeszcze przed importami.

### 🔴 Ćwiczenie

# W poprzednim ćwiczeniu dodaj docstring dokumentujący cały program oraz funkcję print_raport. Jakie informacje umieścisz w dokumentacji?