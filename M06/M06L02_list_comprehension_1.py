### 🔴 Więcej o wyrażeniach listowych

# Znasz już wyrażenia listowe. Poniższy kod:

phones = ['+48123456789', '+4800000000', '+49123456789']
countries = []
for phone in phones:
    country = phone[:3]
    countries.append(country)
print('countries =', countries)  # ==> countries = ['+48', '+48', '+49']

# Możesz zastąpić znacznie krótszym:

countries = [phone[:3] for phone in phones]
print('countries =', countries)  # ==> countries = ['+48', '+48', '+49']

# Jednak co, gdy dodatkowo chcesz pozbyć się części elementów? Co z poniższym kodem?

phones = ['+48123456789', '+4800000000', '+49123456789']
polish_numbers = []
for phone in phones:
    if phone[:3] == "+48":
        short_phone = phone[3:]
        polish_numbers.append(short_phone)
print('polish_numbers =', polish_numbers)  # ==> polish_numbers = ['123456789', '00000000']

# Ten kod również można przepisać, używając nieco bardziej rozbudowanej wersji list comprehension, składni [_ for _ in _ if _]

polish_numbers = [phone[3:] for phone in phones if phone[:3] == "+48"]
print('polish_numbers =', polish_numbers)  # ==> polish_numbers = ['123456789', '00000000']

### 🔴 Ćwiczenie

# Mając podaną listę plików znajdź tylko te, które mają rozszerzenie ".txt".

# Uwaga - zakładamy, że mamy już pewną listę plików, więc nie możemy użyć funkcji glob.glob.

# Rozszerzenie pliku możesz sprawdzić znacznie szybciej, niż robiliśmy to do tej pory. W końcu wystarczy sprawdzić, czy napis kończy się na ".txt". Jak to zrobisz? Poszukaj. :)

# Napisz testy!

files = ['pierwszy.txt', 'drugi.txt', 'ten powinien być usunięty.zip']