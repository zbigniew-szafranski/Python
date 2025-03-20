# Napisz program, w którym definiujesz listę wydatków (w postaci listy liczb), a następnie wyświetlasz ile wyniosły Cię wszystkie wydatki razem.
expenses = [10, 20, 30, 40]
print("PIERWSZE ROZWIĄZANIE")
print('suma wydatków:', sum(expenses))

total = 0
for expens in expenses:
    total += expens
print('Drugie rozwiązanie to suma:', total)