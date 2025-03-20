### 🔴 Czy w Pythonie jest null?

# Czasami potrzebujemy specjalnej wartości oznaczającej, że np. nie mamy pewnych danych, albo że ma być użyta domyślna wartość. W takim sytuacjach używamy None.
# Tak było chociażby w tym programie:

# ❌ źle
args = ['pierwszy', 'drugi', '']
try:
    third = args[2]
except IndexError:
    third = ''
print('third =', third)  # ==> third = <pusty napis>

# W tej sytuacji nie jesteśmy w stanie odróżnić, czy został podany pusty argument '', czy może nie został on podany w ogóle. W obu przypadkach third == ''. Dlatego potrzebujemy osobnej, specjalnej wartości. Teoretycznie moglibyśmy użyć False albo True albo jakieś liczby (np. 0), ale byłoby to mylące. Dlatego używamy None:

# ✅ dobrze
args = ['pierwszy', 'drugi', '']
try:
    third = args[2]
except IndexError:
    third = None
print('third =', third)  # ==> third = <pusty napis>

# Później dokonujemy sprawdzenia, czy mamy None czy coś innego operatorem `is`:

if third is None:
    print('Nie podano argumentu')
else:
    print('Podano:', third)  # ==> Podano: <pusty napis>
    
# 1, 5 i 10 są typu int. "Jan" i "napis" są typu str. False i True są typu bool. Jakiego typu jest None?

print('type(None) =', type(None))  # ==> type(None) = <class 'NoneType'>
    
# Tak, None jest obiektem zupełnie osobnego typu - nie jest ani int'em, ani stringiem, ani boolean'em. Jest specjalnego typu NoneType.
# Tak, mamy klasę/typ NoneType, który ma tylko jedną wartość (= jeden obiekt tego typu) i jest nim None.
# Dla porównania, typ boolean ma dwie wartości - False i True.
# Typy str i int mogą mieć nieskończenie wiele wartości.

### 🔴 Ćwiczenie

# Rozwiń program z M04L12 tak, aby potrafił odróżnić brak rozszerzenia (np. "plik") od pustego rozszerzenia (np. "plik.").