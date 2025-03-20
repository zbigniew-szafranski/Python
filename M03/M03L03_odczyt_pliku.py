### 🔴 Wchodzimy do strumienia (załóż cholewki!)

# Strumienie to pewna abstrakcja/koncept, który pozwala na wczytanie zawartości pliku, a także na zapis do pliku (o tym w kolejnych lekcjach).

### 🔴 Nazwy plików, ścieżki względne i bezwzględne.

filename = 'plik.txt'
path = r'folder\plik.txt'  # to jest ścieżka względna - czyli względem folderu, w którym jesteś w terminalu; wersja na Windowsa
# Na Windowsie katalogi rozdzielamy backslashem \, natomiast na Linuxie i MacOSie slashem /
path = 'folder/plik.txt'  # wersja na Linuxa i MacOS
path = r'C:\katalog\plik.txt'  # ścieżka bezwględna - nie ma znaczenia, który katalog jest "otwarty" w terminalu

### 🔴 1. Otwarcie strumienia

stream = open('M03/plik.txt', 'r')  # plik otwieramy w trybie 'r' - czyli do odczytu (read)
stream = open('M03/plik.txt')  # domyślny tryb to 'r', więc można go pominąć
# stream = open(r'katalog\plik.txt')  # ✅ można podać nie tylko nazwę pliku, ale też ścieżkę względną
# stream = open(r'C:\plik.txt')  # ✅ a nawet ścieżkę bezwględną
# stream = open('nieistniejacy.txt')  # ❌ próba otwarcia pliku, który nie istnieje da nam wyjątek FileNotFoundError

### 🔴 2. Praca z otwartym strumieniem

print('stream =', stream)
print('type(stream) =', type(stream))

# Strumień to osobny typ/klasa, więc mają swój własny zestaw metod.

content = stream.read()  # wczytaj całą zawartość pliku
print('content =', content)
print('type(content) =', type(content))

empty = stream.read()  # ❌ częsta pułapka - ponowne czytanie z tego samego strumienia
print('empty =', empty)

### 🔴 3. Zamykanie strumienia

stream.close()  # dobrą praktyką jest zamykanie strumienia - to jest informacja dla systemu operacyjnego, że już nie potrzebujemy danego pliku; dzięki temu mogą z niego korzystać inne aplikacje

# stream.read()  # ❌ na zamkniętym strumieniu nie można już wykonać żadnych operacji

### 🔴 Ćwiczenie

# Rozwiń program z M02L11. Tamten program pytał użytkownika o tekst do zanonimizowania, czyli zastępował wszelkie występujące tam liczby iksami, np. 1234 -> XXXX. Tym razem zapytaj użytkownika o nazwę pliku (np. plik.txt) i wczytaj tekst właśnie z niego. Zanonimizuj go, a następnie wyświetl na ekranie.