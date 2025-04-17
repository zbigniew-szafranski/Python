# . Napisz funkcję abs, która zwraca wartość bezwzględną liczby. To znaczy, że dla liczby ujemnej zwraca tę liczbę bez znaku, czyli dodatnią:
#
# abs(5) == 5
#
# abs(-3) == 3
x = 4


def print_abs(x):
    if x < 0:
        return -x
    else:
        return x

def main():
    x=-4
    print(abs(x))


if __name__ == "__main__":
        main()