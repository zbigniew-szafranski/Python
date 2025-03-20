### 🔴 IPython (nie, nie od Apple)

# Tym razem poznamy interaktywną konsolę. Uruchom Pythona bez podania skryptu:

# $ python

# W ten sposób uruchamiasz tzw. INTERAKTYWNĄ KONSOLĘ, w której możesz wprowadzać kod i od razu widzieć jego rezultaty.

# Aby z niej wyjść, wpisz exit() lub wciśnij ctrl+C (lub ctrl+D).

# Ta konsola jest jednak dosyć nieporęczna - nie ma nawet kolorowania składni. Dlatego opracowano lepszą konsolę, która trzeba jednak doinstalować:

# $ pip install ipython

# Teraz można ją wystartować:

# $ ipython

### 🔴 Uruchomienie skryptu + włączenie interaktywnej konsoli

# Do tej pory programy uruchamialiśmy od początku do końca. Nie mieliśmy wglądu w kod w trakcie jego wykonania - nie mogliśmy nagle dodać jednej linii kodu albo wyświetlić wartość danej zmiennej.

# Bardzo przydatną kombinacją jest wykonanie skryptu, a następnie uruchomienie interaktywnej konsoli, aby mieć wgląd w wartości zmiennych, żeby wywołać funkcje zdefiniowane w tym skrypcie albo żeby w inny sposób poeksperymentować.

# W tym celu uruchamiamy skrypt podając przełącznik -i - koniecznie przed nazwą skryptu!

# $ python -i M05/M05L14_ipython.py
# $ ipython -i M05/M05L14_ipython.py  # a najlepiej użyć ipython'a

# W ten sposób uruchomimy ten skrypt:

import sys

STALA = 'const'

def funkcja(msg):
    print(f'Msg: {msg}')
    
# A następnie w interaktywnej konsoli możemy:

# - podejrzeć wartości zmiennych - print(STALA)
# - wywoływać funkcje - funkcja("Komunikat")
# - wykonywać dowolny kod Pythona - 2 + 2

# I najważniejsze nowe możliwości:

# - podejrzeć jakie są funkcje lub metody dzięki INTROSPEKCJI - sys. [wciśnij przycisk tab]
# - uzyskać informacje o danym module, funkcji lub metodzie przez INTROSPEKCJĘ (przez wgląd) - help(sys)

# INTROSPEKCJA oznacza, że Python patrzy na moduł taki, jaki jest załadowany do pamięci. Jest to podejście inne do tego, co robi VSCode - on z kolei analizuje kod (bez wykonywania kod) i wyciąga z niego docstring. To podejście nie wymaga uruchamiania kodu, ale z drugiej strony nie zawsze daje tak dobre rezultaty jak introspekcja.

# Dzięki temu jeśli wszystko sprzysięgnie się przeciwko nam i:
# 1) VSCode nie podpowiada listy funkcji lub metod, nie widzi docstringów i ich nie wyświetla
# 2) jednocześnie nie ma dokumentacji w internecie lub nie ma tam szukanej przez nas informacji
# 3) jednocześnie nie ma tej informacji na StackOverflow
# to wciąż możemy uzyskać trochę informacji o danym kodzie - albo przez introspekcję, albo przez eksperymentowanie z kodem.

# Wykorzystując funkcję help() możemy nawigować strzałkami, szukać przy pomocy slasha / i wyjść przy pomocy q.

### 🔴 Ćwiczenie

# 1. Uruchom poniższy program w interaktywnej konsoli IPython z przełącznikiem -i. 

# 2. Spróbuj w konsoli wyświetlić dokumentację dla modułu `html` przy pomocy funkcji help().

# 3. W ten sposób spróbuj znaleźć funkcję służącą do parsowania HTML - dokładnie to samo, co zrobiłaeś w poprzednim ćwiczeniu, tylko tym razem ćwiczymy to w interaktywnej konsoli.

# 4. W kolejnym ćwiczeniu wykorzystasz nabyte teraz umiejętności w znajdowaniu nowych, nieznanych Ci jeszcze funkcjonalności.

from lxml import html