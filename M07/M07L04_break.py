### 🔴 Instrukcja break

# Funkcja eval
result = eval('2+2')
print('result =', result)
print('type(result) =', type(result))

# Przykładowy REPL - Read-Eval-Print Loop.
while True:
    expr = input('>>> ')
    if expr.lower().strip() == 'exit':
        break  # Instrukcja break natychmiast przerywa wykonywanie pętli i przenosi nas za pętle do 'Finish'
    result = eval(expr)
    print(result)
print('Finish')

### 🔴 Ćwiczenie

# Pracujesz dla Google i jesteś odpowiedzialny za rozwój przeglądarki Google Chrome.
# Twoim zadaniem jest napisać moduł odpowiedzialny za pobieranie plików.
# W momencie pobierania pliku "plik.txt" zapisujesz go na dysku dokładnie pod tą samą nazwą, CHYBA ŻE już taki plik istnieje.
# W takiej sytuacji nie chcesz go nadpisać, dlatego zapisujesz plik pod nazwą "plik-2.txt".
# Jeśli ta nazwa również jest już zajęta, to zapisz do pliku "plik-3.txt" itd.
# Twoim zadaniem jest napisać funkcję, która otrzymuje nazwę pliku i zwraca tą nazwę z doklejoną odpowiednią końcówką "-2", "-3" itd., tak żeby nie nadpisać żadnego pliku.
# Jakiej funkcji użyjesz do sprawdzenia, czy plik już istnieje?
# Napisz testy! W jaki sposób przetestujesz swój kod?