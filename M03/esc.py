# Stwórz i wydrukuj string, który zawiera:
# 1. cudzysłów " (np. tekst w "cudzysłowie"), a także
# 2. apostrof ' (np. I'm happy).
# W jaki sposób umieścisz te znaki?

# print("\"to jest tekst w cudzysłowie\" a to A'postrof")
text = input("Podaj ścieżkę do pliku: ")

with open(text) as stream:
    content = stream.read()

for digit in '0123456789':
    content = content.replace(digit,'X')
    
print(content)