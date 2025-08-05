### 🔴 Ćwiczenie
# Napisz program, który prosi o jeden, pojedynczy znak, a następnie sprawdza, czy jest to litera, czy coś innego. Ponownie, tak jak w jednym z poprzednich ćwiczeń, musisz znaleźć odpowiednią metodę, która sprawdza, czy dany napis to litera.

character = input("Podaj jeden znak, aby określić, czy to jest litera: ")
if len(character)==1:
    if character.isalpha():
        print("Ten znak jest literą")
    else:
        print("Ten znak nie jest literą")
else:
    print("Ma być jeden znak")