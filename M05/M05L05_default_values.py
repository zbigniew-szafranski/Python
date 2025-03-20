### 🔴 Wartości domyślne

# Wywołując funkcję musisz przekazać odpowienią liczbę parametrów - ani nie za mało, ani nie za dużo.

def chce_jeden_parametr(param):
    print(param)
    
chce_jeden_parametr(1)  # ✅ ok
# chce_jeden_parametr()  # ❌ źle ==> TypeError: chce_jeden_parametr() missing 1 required positional argument: 'param'
# chce_jeden_parametr(1, 2)  # ❌ źle ==> TypeError: chce_jeden_parametr() takes 1 positional argument but 2 were given

# Co jeśli chcemy mieć OPCJONALNY parametr z wartością domyślną? Możemy podać wartość domyślną i wtedy ten parametr staje się opcjonalny. 

def add(a, b, force_conversion=False):
    if force_conversion:
        a = float(a)
        b = float(b)
    return a + b

print(add('5', '8', False))
print(add('5', '8', True))
print(add('5', '8'))  # ✅ też jest ok

# Parametry opcjonalne muszą znaleźć się PO wszystkich parametrach wymaganych. Dlatego poniższy kod nie zadziała:

# def nie_zadziala(pierwszy_wymagany, opcjonalny=None, drugi_wymagany):  # ❌ nie zadziała
#     print('BUM')

### 🔴 Ćwiczenie

# Usprawnij kod z ćwiczenia M05L03. Zrób tak, aby inne skrypty mogły zaimportować Twój program i skorzystać z jego funkcjonalności - dokładnie tak jak w M05/M05L05_dodatek.py.

# Dzięki temu gdy ktoś będzie chciał ponownie użyć Twojego programu, może go nie tylko uruchomić w terminalu, ale może także go zaimportować i wywołać nową funkcję print_raport(filenames, ignore_missing). 

# Nazwy plików (filenames) oraz przełącznik (ignore_missing) powinny być w tej funkcji przekazane jako parametry. Przy czym drugi parametr powinien być opcjonalny. Jaką wybierzesz domyślną wartość?

# W osobnej funkcji main() wywołaj funkcję print_raport przekazując wartości dla tych dwóch parametrów z sys.argv.