### 🔴 Uruchomienie vs import

# from M05L02_bad_library import generate_username
from M05L02_good_library import generate_username  # importujemy funkcję z modułu M05L02 z pakietu M05

# Załóżmy, że napisałæś już wcześniej moduł M05L02_bad_library, który w funkcji generate_username implementuje funkcjonalność generowania nazw użytkownika (brak spacji i tylko małe litery). (O funkcjach będziemy mówić później w tym tygodniu). Ten moduł można uruchomić jako skrypt - wówczas prosi o imię i nazwisko i generuje nazwę użytkownika:

# $ python M05/M05L02_bad_library.py

# Teraz przyszła pora napisać program, który generuje nazwy użytkowników dla całego pliku. Ten skrypt M05L02_name wczytuje osoby z pliku i generuje dla nich nazwy użytkownika.

# Chcemy wykorzystać funkcję generate_username z tego modułu. Wiesz już, że kiedy uruchamiasz skrypt, jego kod jest wykonywany od góry do dołu i że dokładnie to samo dzieje się gdy IMPORTUJESZ ten skrypt. Jednak w przypadku importu nie chcesz odpalać kodu z samego końca tego modułu, chcesz jedynie zaimportować funkcje.

# Dlatego kod na samym końcu M05L02_bad_library powinien być wykonywany TYLKO gdy skrypt jest uruchamiany, ale nie gdy jest importowany. Jak rozróżnić te dwie sytuacje?

# Użyj specjalnej zmiennej __name__, która jest dostępna w każdym module. Pod tą zmienną kryje się nazwa aktualnego modułu, np. "M05L02_name" albo "M05L02_bad_library", CHYBA ŻE jest to ten moduł, który został uruchomiony w terminalu. Wówczas pod tą zmienną kryje się specjalna wartość "__main__".

# Możesz rozróżnić, czy masz do czynienia z uruchomieniem a nie importem dzięki linii if __name__ == "__main__".

# Zerknij jak to jest zrobione w M05L02_good_library.

# Dobrą praktyką jest stosowanie takiego if'a w KAŻDYM skrypcie, którego jakiś kod powinien być wykonywany tylko w przypadku uruchomienia, a nie importu. Wyrób sobie nawyk stosowania tej dobrej praktyki.

# $ python M05/M05L02_name.py M05/users.txt

import sys

print(f"M05L02_main.__name__ =", __name__)

filename = sys.argv[1]
with open(filename) as stream:
    content = stream.read()
    
for name in content.split('\n'):
    username = generate_username(name)
    print(f"{name} -> {username}")

### 🔴 Ćwiczenie

# 1. Ten if należy stosować w KAŻDYM skrypcie - także tutaj, w pliku M05L02_main. Popraw ten plik.
# 2. Przepisz program "word count" z M04L15 tak, aby jego kod był wykonywany tylko podczas URUCHOMIENIA programu, a nie podczas jego IMPORTU.