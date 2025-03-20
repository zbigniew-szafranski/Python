### 🔴 Escaping, czyli jak uciekać?

# W kolejnych lekcjach będziemy pracować na plikach. Pojawią się ścieżki do plików, a to wymaga poruszenia tematu escapingu.

# text = "jedna linia
# druga linia"  # ❌ to nie zadziała => SyntaxError (błąd składni)
text = "jedna linia\ndruga linia"  # backslash \ ma specjalne znaczenie, służy do wstawiania szczególnych znaków, np. \n oznacza nową linię
print('text =', text)

backslashes = "jak wstawić backslash? \\ to będzie jeden backslash"
print('backslashes =', backslashes)

path = "C:\\katalog\\plik.txt"  # ścieżki Windowsowe wymagają podwójnego backslasha - niewygodne :-( , czy można prościej?
print('path =', path)

convenient_path = r"C:\katalog\plik.txt"  # można, wystarczy użyć r"" zamiast "" - wówczas wyłączamy mechanizm escapowania
print('convenient_path =', convenient_path)

escaping_disabled = r"Ten tekst\nbędzie\nw jednej linii."
print('escaping_disabled =', escaping_disabled)

### 🔴 Ćwiczenie

# Stwórz i wydrukuj string, który zawiera:
# 1. cudzysłów " (np. tekst w "cudzysłowie"), a także
# 2. apostrof ' (np. I'm happy).
# W jaki sposób umieścisz te znaki?