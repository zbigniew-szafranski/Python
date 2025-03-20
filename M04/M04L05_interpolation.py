### 🔴 Jak szybko i prosto wyświetlać tabele?

# Normalnie w stringach klamry są wyświetlane jako klamry:

pesel = 12345678901
name = 'Jan Kowalski'
print("{pesel} {name}")  # ==> {pesel} {name}

# Jeśli możesz włączyć string interpolation/formatting używając litery f:

print(f"{pesel} {name}")  # ==> 12345678901 Jan Kowalski

# Między klamrami podajemy nazwę zmiennej - lub nawet całe wyrażenie! 

print(f"{name.lower()}")  # ==> jan kowalski

# Co więcej, możesz po nim dodać dwukropek i określić szczegóły jak dana zmienna ma być wyświetlona. Możesz podać ile minimalnie znaków szerokości powinna mieć ta zmienna:

print(f"{pesel:13} {name}")  # ==>   12345678901 Jan Kowalski  # (!) dwie spacje na początku

# Po dwukropku można określić bardzo dużo szczegółów, w szczególności:

# - wyrównanie (dla liczb domyślnie do prawej, w pozostałych przypadkach do lewej), 
# - liczbe cyfr po przecinku dla liczb niecałkowitych,
# - typ danych i sposób ich wyświetlenia (np. liczba całkowita, liczba niecałkowita, liczba w zapisie binarnym, notacji naukowej etc.)

# Więcej znajdziesz w dokumentacji: https://docs.python.org/3/library/string.html#formatspec

### 🔴 Ćwiczenie

# Rozwiń program z poprzedniej lekcji tak, aby wyniki wyświetlić w tabeli. Użyj string interpolation. Dodaj nagłówek tabeli.