### 🔴 Unikalne elementy

# Znasz już dwie kolekcje - listę (list) oraz słownik (dict).
# Lista jest jak arkusz z jedną kolumną, a dict zapewnia unikalność kluczy.
# Czasami chcesz połączyć jedno z drugim - mieć listę UNIKALNYCH elementów, czyli bez powtórzeń.
# Taką kolekcją jest SET (zbiór)
# Tutaj również wykorzystujemy klamry, tak jak w słownikach!

my_set = {1, 2, 3, 1}
print('my_set =', my_set)  # ==> {1, 2, 3}

# Jednak najczęściej zbiór tworzymy mając już inną kolekcję - używamy wtedy funkcji set():

text = 'ile razy pojawia się słowo ile w tym tekście'
words = text.split()
unique = set(words)
print('words =', words)  # words jest dalej listą z powtórzeniami!!! set nie ruszy listy, tylko zwraca nowy zbiór 
print('unique =', unique)

# Uwaga! Zbiór nie pamięta kolejności elementów! Jest to WOREK wartości, a nie uporządkowana lista! Słowniki i listy pamiętają kolejność.

### 🔴 Ćwiczenie

# W projekcie M03L19 analizowaliśmy sentyment 25 tys. recenzji filmowych. Wymagało to m.in. zliczenia w ilu recenzjach pojawiają się poszczególne słowa. W pierwotnym rozwiązaniu prosiliśmy użytkownika o nową recenzję, dzieliliśmy ją na słowa, a następnie dla każdego słowa przechodziliśmy przez wszystkie recenzje, aby zliczyć ile razy to słowo pojawia się w negatywnych, a ile razy w pozytywnych komentarzach.
# Nie jest to najefektywniejszy sposób. W tym ćwiczeniu poprawisz kod z tamtego projektu tak, aby na etapie wczytywania plików zliczył liczbę wystąpień poszczególnych słów, zapamiętał rezultat w dwóch osobnych słownikach (jeden dla pozytywnych recenzji, jeden dla negatywnych). Następnie poproś użytkownika o nową recenzję i wylicz jej sentyment korzystając już tylko z tych dwóch słowników.
# Zwróć uwagę, że nawet jeśli jakieś słowo pojawia się w recenzji dwa razy, wówczas jego licznik chcemy zwiększyć tylko o jeden. W końcu interesuje nas liczba recenzji zawierających dane słowo, a nie ile razy to słowo pojawia się we wszystkich recenzjach. Potrzebujemy więc w ramach pojedynczej recenzji pozbyć się powtórzeń tych samych słów.

# Dzięki tym modyfikacjom program wykorzystuje mniej pamięci, bo nie musi zapamiętywać wszystkich recenzji w pamięci, a jedynie liczbę wystąpień słów.
# Po drugie, program będzie dużo szybciej wyliczał sentyment nowych recenzji. W wielu zastosowaniach Machine Learning kluczowe jest, aby czas predykcji (czyli czas wyliczania sentymentu dla nowej recenzji) był wystarczająco krótki.