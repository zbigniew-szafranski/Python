### 🔴 Ćwiczenie

# Napisz program, który anonimizuje dane statystyczne w tekstach poprzez zastąpienie wszelkich liczb iksami.

text = input('Podaj text: ')
for digit in "0123456789":
    text = text.replace(digit, 'x')
print('Zaniminizowany tekst: ', text)