### 🔴 Programowanie obiektowe

# W module 4 przetwarzaliśmy listę wydatków - gdzie każdy wydatek miał pewną kwotę oraz opis. Każdy wydatek możemy opisać jako listę:

expense = [6.50, "Ziemniaki"]

# Jednak ten sposób jest bardzo toporny - musimy pamiętać, pod którym indexem jest cena i pod którym jest opis. Lepszym rozwiązaniem są słowniki:

expense = {
    'amount': 6.50,
    'description': "Ziemniaki",
}

# Na słownikach operuje się dużo lepiej. Gdybyśmy mieli przesłać nasze wydatki gdzieś w świat, to pewnie użylibyśmy słowników, skonwertowalibyśmy je na JSON i wysłali w świat.

# Jednak w samym programie jeszcze lepiej jest je przechowywać jako obiekty WŁASNEJ KLASY.

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
e = Expense(6.5, "Ziemniaki")  # to wywołuje metodę __init__() i tworzy nowy OBIEKT KLASY Expense 
# self jest automatycznie dodawany przez Pythona!

# Kilka rzeczy, o których warto pamiętać:

# 1. Funkcje w środku klasy to METODY.

# 2. Metody specjalne to metody zaczynające się i kończące dwoma podkreśleniami, np. __init__ albo __repr__.

# 3. Najważniejszą metodą specjalną jest __init__, który jest wywoływany gdy tworzysz nowy obiekt.

# 4. Przy wywoływaniu metod obowiązują te same zasady co przy wywoływaniu funkcji, czyli argumenty można przekazywać w sposób zarówno pozycyjny, jak i nazwany:

e = Expense(6.5, desc="Ziemniaki")

# 5. Nie musimy zawczasu określać, jakie POLA będą mieć obiekty - po prostu tworzymy je DYNAMICZNIE w __init__.

# Teraz możemy korzystać z takiego obiektu:

print('e.amount =', e.amount)
print('e.description =', e.description)

### 🔴 Ćwiczenie

# Popraw kod z ćwiczenia M03L16. W tym ćwiczeniu zmienialiśmy rozszerzenia wielu plików na raz. 

# Po pierwsze, zastosuj nowe dobre praktyki, które poznałæś w czwartym i piątym module.

# Po drugie, w tym programie tworzyliśmy listę wszystkich operacji do wykonania. Każdą operację reprezentowaliśmy jako dwuelementowa lista [obecna_nazwa_pliku, nowa_nazwa_pliku].

# Dużo lepiej jest reprezentować operację jako obiekt własnej klasy RenameOperation.

# Stwórz taką klasę i przepisz kod tak, aby ją wykorzystywał.