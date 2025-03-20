# Napisz program, który prosi o jeden, pojedynczy znak, a następnie wyświetla, czy jest to liczba, litera, biały znak czy znak specjalny.
# Białe znaki to spacja, tabulacja i nowa linia.

char =input('Podaj pojedynczy znak: ')
if len(char)==1:
    if char.isalpha():
        print('Jest to litera')
    elif char.isalnum():
        print('Jest to liczba')
    elif char.isspace():
        print('Biały znak')
    else:
        print('Znak specjalny')
else:
    print('Prośba była o jeden znak')