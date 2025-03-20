### 🔴 Teoria

# Co gdy w projekcie A potrzebujesz flask'a w wersji 2.0, a projekcie B w wersji 1.1?
# Przełączając się między tymi projektami musisz za każdym razem odinstalować poprzednią wersję i zainstalować odpowiednią wersję flaska - każda paczka może być zainstalowana tylko w jednej wersji. 
# Dlatego wymyślono tzw. virtualenv'y, czyli lekkie "kopie" Pythona.
# Oprócz GLOBALNEGO środowiska możesz stworzyć dowolną liczbę wirtualnych środowisk. Każde wirtualne środowisko jest niezależne od pozostałych oraz od globalnego.

### 🔴 Praktyka

# Tworzenie venva
# $ python -m venv my_venv
# $ python --version  # dalej aktywna jest globala instalacja

# Aktywowanie venva
# $ source my_venv/bin/activate  # Linux/MacOS
# $ my_venv\Scripts\activate.bat  # Windows
# $ python --version  # tym razem aktywny jest nasz venv

# Instalacja paczek i uruchamianie - dokładnie tak jak do tej pory
# $ python script.py
# $ pip install flask --upgrade  # instalacja najnowszej wersji
# $ pip install flask==1.0  # instalacja konkretnej wersji

# Deaktywacja venva
# $ deactivate

# Praca z virtualenvami w VSCode - polecenie "Python: Select Interpreter".
# Wskazujemy plik my_venv\Scripts\python.exe, a nie sam katalog my_venv!

### 🔴 Ćwiczenie

# 1. Stwórz dwa virtualenvy.
# 2. W pierwszym zainstaluj najnowszą wersję paczki flask.
# 3. W drugim zainstaluj paczkę flask w najnowszej wersji 1.1.X.
# 4. Upewnij się, jaka wersja jest zainstalowana w każdym z virtualenvów? Jaka wersja jest zainstalowana w globalnym środowisku?
# 5. Napisz program z poniższym kodem i uruchom go w VSCode w każdym z dwóch virtualenvów.

import flask
print(flask.__version__)