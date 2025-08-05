### 🔴 Ćwiczenie
# Napisz program, który prosi użytkownika o hasło, a następnie dla każdego znaku wyświetla jakiego typu jest to znak (litera vs cyfra vs biały znak vs znak specjalny).
password = input("Podaj hasło: ")

for char in password:
    if char.isalpha():
        type_ = 'litera'
    elif char.isalnum():
        type_ = 'liczba'
    elif char.isspace():
        type_ = 'biały znak'
    else:
        type_ = 'znak specjalny'
    print(char, type_)
