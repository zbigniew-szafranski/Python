### 🔴 Funkcja main

# Funkcje można WYWOŁYWAĆ (= korzystać z istniejących) jak i DEFINIOWAĆ (= tworzyć własne funkcje).

# Do tej pory jedynie wywoływaliśmy wbudowane funkcje. Tym razem zdefiniujemy własne funkcje.

# Funkcje zmieniają kolejność wykonywania kodu, co widać poniżej. W momencie wywołania funkcji zapamiętujemy gdzie to nastąpiło, następnie skaczemy do funkcji, wykonujemy jej kod od góry do dołu, a potem wracamy tam, skąd ją wywołaliśmy:

def foo():
    print('Foo')

print("Początek")
foo()
print("Koniec")

# Przy czym w środku funkcji można wywoływać kolejne. Trzeba wówczaś śledzić skąd gdzie trzeba wrócić - jest to realizowane na tzw. STOSIE WYWOŁAŃ.

def spam():
    print('W środku spam')

def egg():
    print('Początek egg')
    spam()
    print('Koniec egg')

print()
print("Początek")
egg()
print("Koniec")

# W momencie gdy w kodzie nastąpi błąd, wyświetlany jest stacktrace, czyli właśnie ten stos wywołań:

def dziel_przez_zero():
    print('Zaraz będzie BUM!')
    print(1 / 0)  # ==> ZeroDivisionError

def zlec_dzielenie_przez_zero():
    print('Zlecam dzielenie przez zero')
    dziel_przez_zero()
    print('Dzielenie przez zero zakonczone')

print()
print("Początek")
zlec_dzielenie_przez_zero()
print("Koniec")

### 🔴 Ćwiczenie

# Przepisz kod z poprzedniego ćwiczenia tak, aby całość kodu umieścić w funkcji main(). Jest to również pewna dobra praktyka (chociaż stosowana rzadziej niż sprawdzanie wartości __name__).