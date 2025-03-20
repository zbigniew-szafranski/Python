### 🔴 Praktyczne zastosowania funkcji

# Dlaczego właściwie warto korzystać z funkcji?

# 1. Funkcje przydają się do unikania duplikacji podobnego (lub wręcz identycznego) kodu!
# Jeśli robisz copy-paste w swoim kodzie, to prawdopodobnie warto stworzyć funkcję z tego fragmentu, który skopiowałæś.
# Stosuj zasadę DRY = Don't repeat yourself!

# 2. Funkcje przydają się do uniknięcia duplikacji kodu w przyszłości!
# Jeśli dzielisz swój kod na funkcje i dbasz, aby każda funkcja robiła tylko jedną rzecz, wówczas w przyszłości bardzo łatwo będziesz mógł/mogła ponownie wykorzystać zaimplementowaną już funkcjonalność. I to bez modyfikowania kodu, który chcesz wywołać!

# 3. Funkcje pozwalają na ukrycie szczegółów i opisanie kodu z lotu ptaka.

def load_files():
    # A lot of lines of code...
    return ['many', 'many', 'files']

def preprocess_files(files):
    print('Preprocessing')
    # A lot of lines of code ...
    return 'preprocessed files'
    
def train_machine_learning_model(data):
    # A lot of lines of code
    return 'trained model'

def save_model(model):
    # A lot of lines of code...
    print('Saving model')
    
def main():
    # ✅ tutaj mamy opis z lotu ptaka - bez wdawania się w szczegóły
    files = load_files()
    preprocessed = preprocess_files(files)
    model = train_machine_learning_model(preprocessed)
    save_model(model)
    
# Hint: Jeśli widzisz blok kodu zaczynający się komentarzem, to znaczy że może warto z tego bloku stworzyć funkcję?    
    
# 4. Funkcje ułatwiają testowanie kodu - zarówno manualne, jak i automatyczne. O testowaniu automatycznym powiemy na końcu modułu.

### 🔴 Ćwiczenie

# Zerknij na rozwiązanie ćwiczenia M04L08. Znajduje się tam trochę powtórzonego kodu.
# 1. Użyj funkcji, aby uniknąć duplikacji kodu.
# 2. Popraw kod tak, aby miał funkcję main().
# 3. Czy widzisz jakieś bloki kodu zaczynające się od komentarza podsumowującego, co robi dany blok? Jeśli tak, to jak możesz zwiększyć czytelność kodu poprzez wprowadzenie nowych funkcji?