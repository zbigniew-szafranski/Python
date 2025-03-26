# Rozwiń program z M03L07. Tym razem format pliku jest następujący: każda linia to jeden wydatek. Najpierw jest kwota wydatku, a po spacji jego opis. Opis może zawierać kolejne spacje. Plik może zawierać puste linie. Przykładowy plik to expenses-ex.txt
# W tym ćwiczeniu nie wystarczy, aby skorzystać ze .split(), dlatego że ono dzieli nie tylko na poszczególne linie, ale także po spacjach w każdej linii. Tutaj konieczne jest dzielenie tylko po znakach nowej linii. Jak to zrobić? Da się to zrobić używając .split(), ale trzeba przekazać pewien parametr. Doczytaj w dokumentacji jak dokładnie to zrobić.
# Mając już pojedynczą linię konieczne będzie dalsze jej podzielenie już po spacjach, tak aby dostać się do kwoty wydatku, która jest na początku każdej linii.

EXPENSES_FILENAME = 'M03/expenses_ex.txt'
with open(EXPENSES_FILENAME) as stream:
    content = stream.read()
lines = content.split('\n')
total = 0
for line in lines:
    token = line.split()
    if token:
        expense = token[0]
        total+=float(expense)
print("Kwota wydatków: ", total)
