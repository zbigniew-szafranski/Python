### 🔴 Co mają wspólnego przepisy kulinarne i programowanie?

# 👉 Skończyłæś większość tego tygodnia - gratulacje! Masz już wszystko skonfigurowane.
# 👉 Przechodzimy do drugiej, krótszej części tego tygodnia - do kodowania.

### 🔴 Funkcje

# 👉 Funkcje są jak przepisy kulinarne. DEFINIOWANIE własnych funkcji w kolejnych modułach.
# 👉 Dzisiaj jak WYWOŁYWAĆ (=używać) wbudowane funkcje

### 🔴 Niezbędnik

# Składnia wywołania: nazwa_funkcji ( argumenty )

print(1234)

print("tekst")

text = "tekst"
print(text)

# Niektóre funkcje mogą przyjmować więcej argumentów - rozdziel je przecinkiem.
print("tekst", "wiecej tekstu")

# Niektóre funkcje nie przyjmują żadnych argumentów - wtedy nawiasy też są konieczne!
print()  # print bez argumentów przechodzi do następnej linii

# ❌ Typowa pułapka - brakuje nawiasów okrągłych, w efekcie ta linia kodu nie robi nic, ale nie ma błędu!
print

# Parametry funkcji to to samo co jej argumenty. Jest to synonim. (ok, zgoda, jest subtelna różnica o której w jednym z kolejnych modułów).

# Funkcje mogą zwracać wartość - rezultat swojego działania.
dlugosc = len(text)  # Funkcja len zwraca długość napisu przekazanego jako argument.
print(dlugosc)

# W jednej linii można złożyć kilka wywołań funkcji (tzw. composability)
print(len(text))

# ❌ Nie można zagnieżdżać przypisania.
# print(text = "tekst")

# Niektóre argumenty przekazujemy w sposób nazwany (więcej w module o funkcjach).
# W takiej sytuacji znak równości nie ma nic wspólnego z przypisaniem!
print("liczba:", end=" ")
print(1234)
print(2345)

# Funkcja input wyświetla tekst (tak samo jak print) i prosi użytkownika o jedną linię tekstu. Użytkownik zatwierdza tekst enterem.
tekst = input("Tekst: ")
print("Wpisałeś:", tekst)

### 🔴 Ćwiczenie: Napisz program, który prosi użytkownika o tekst i wyświetla ile ma on liter.

# Wyślij nam swoje zadanie domowe, a zobaczysz rozwiązanie, jego omówienie, na co dobrze było zwrócić uwagę, a także najczęstsze błędy.
tekst2 = input("Podaj tekst do obliczenia długości:")
print("Długość", len(tekst2), "znaki")

# #1
text = "Wypisuję tekst"
print(text)

# #2
print("tekst", "wiecej tekstu")

# #3
print(len(text))

# #4
print("tekst", "wiecej tekstu")

# #5
print("liczba:", end=" ")
print(1234)