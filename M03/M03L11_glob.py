### 🔴 Moduły

import glob  # powoduje zaimportowanie biblioteki glob
# Biblioteka glob jest częścią STANDARDOWEJ BIBLIOTEKI, czyli zestawu bibliotek dostępnych w Pythonie out-of-the-box, bez potrzeby doinstalowywania czegokolwiek.
# Istnieją też THIRD-PARTY LIBRARIES i te należy doinstalować - o tym jednak w kolejnych modułach.

print('glob =', glob)
print('type(glob) =', type(glob))

# glob jest modułem, czyli pewną paczką różnych funkcji (a także klas i zmiennych)
# Do tej pory składnia z kropką pozwalała na wywołanie metody: obiekt.metoda(parametry)
# W przypadku modułów kropka pozwala nam na użycie konkretnej funkcji z danego modułu: modul.funkcja(parametry)

files = glob.glob('M03/M03L0*')
print('files =', files)

# glob.glob('*.txt')  # ✅ ok
# glob.glob(r'C:\katalog\*.txt')  # ✅ ok  

### 🔴 Ćwiczenie

# Rozwiń program z poprzedniego ćwiczenia tak, aby znajdować wszystkie pliki pasujące do podanego przez użytkownika wzorca i zmienić ich rozszerzenie na .bak.
# Na ten moment dalej jedynie wyświetl, jaką zmianę byś dokonał(a) - realną zmianą nazwy pliku zajmiemy się w kolejnych lekcjach.