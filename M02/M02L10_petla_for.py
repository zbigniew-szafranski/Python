### 🔴 Powtarzam, powtarzam, powtarzam, powtarzam, powtarzam... Pętla for

# Znasz już rozgałęzienia warunkowe (IF) - ale co z powtarzaniem operacji dla każdego X? Np. dla każdego pliku, dla każdego znaku w napisie etc.

# Przykład
text = "mój tekst"
for char in text:
    # przy pierwszym iteracji char = "m"
    # przy drugiej iteracji char = "ó" itd.
    print(char)

# Składnia: for zmienna in wyrażenie :
# for char in text:  # ✅ ok
# for char + 2 in text:  # ❌ źle
# for char in "mój tekst":  # ✅ ok
# for char in text.lower():  # ✅ ok
# for char in text.lower().replace(' ', '_') + "_sufix":  # ✅ ok
# for char in text  # ❌ brakujący dwukropek

# Nie po każdym obiekcie można ITEROWAĆ, czyli użyć w pętli for. Na ten moment są to tylko stringi.
number = 1234
for char in number:  # ==> TypeError: 'int' object is not iterable
    print(char)

### 🔴 Ćwiczenie
# Napisz program, który prosi użytkownika o hasło, a następnie dla każdego znaku wyświetla jakiego typu jest to znak (litera vs cyfra vs biały znak vs znak specjalny).