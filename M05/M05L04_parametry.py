### 🔴 Czy funkcje muszą zawsze robić to samo?

# Funkcje mogą przyjmować PARAMETRY (= ARGUMENTY). Ich wartość określamy w momencie WYWOŁANIA. Robimy to na codzień, np. stosując funkcję print:

print('Print robi za każdym razem to samo - wyświetla na terminal')
print('Ale dzięki parametrom za każdym razem może wyświetlić co innego.')

# Stwórzmy taką funkcję, która na razie przyjmuje jeden parametr:

def print_username(name):
    username = name.lower().replace(' ', '_')
    print(username)
    
print_username('Jan Kowalski')
print_username('Michał Wiśniewski')

# Co jednak, gdy chcemy zapisać username do zmiennej zamiast wypisać go na ekran? Funkcje mogą nie tylko przyjmować dane (dzięki parametrom), ale mogą też ZWRÓCIĆ wartość:

def generate_username(name):
    username = name.lower().replace(' ', '_')
    return username

my_username = generate_username('Jan Kowalski')
username = generate_username('Michał Wiśniewski')  # nie ma żadnej kolizji

# Funkcja może przyjąć wiele argumentów, ale zawsze zwraca tylko jedną wartość. Jeśli trzeba zwrócić wiele, to wtedy upakuj je w listę i zwróć tą liste. A jak już w przyszłości poznasz krotki (= tuple), to wtedy stosuj krotki.

# Co zwraca funkcja, która nie używa instrukcji return?

result = print_username('Jan Kowalski')
print('result =', result)  # ==> result = None

# Każda funkcja coś zwraca. Jeżeli nie ma w niej instrukcji return, to zwraca None. Niestety, nie ma wtedy błędu, stąd pułapki takie jak ta: ❌

lista = ['first', 'second']
lista = lista.append('third')
print('lista =', lista)  # ==> lista = None

# Albo pułapka taka jak ta: ❌

text = "TEXT let's make it lowercase"
lowered = print(text.lower())  # ==> text let's make it lowercase
print('lowered =', lowered)  # ==> lowered = None

### 🔴 Ćwiczenie

# Usprawnij kod z M04L07 (zliczanie liczby wystąpień poszczególnych słów), tak aby można było ponownie wywołać zawarty tam kod dla dwóch różnych napisów. 
# W tym celu opakuj ten kod w dwie funkcje. Pierwsza funkcja jest odpowiedzialna za samo zliczenie słów i stworzenie słownika counter. Druga funkcja powinna wyświetlać raport mając podany właśnie ten słownik.