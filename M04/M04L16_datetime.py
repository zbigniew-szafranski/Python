### 🔴 Jak pracować z datami?

# Importujemy KLASĘ datetime z MODUŁU datetime:

from datetime import datetime

dt = datetime(2021, 8, 21, 15, 30, 0)

print('dt =', dt)  # ==> dt = 2021-08-21 00:00:00

# Tworząc datetime nie musimy podawać godziny, minuty ani sekundy jeśli interesuje nas tylko data, bez czasu.

dt2 = datetime(2021, 8, 21)

print('dt2 =', dt2)  # ==> dt2 = 2021-08-21 00:00:00

# Jakie metody i atrybuty ma datetime?

print('dt2.day =', dt2.day)  # ==> dt2.day = 21

### 🔴 Ćwiczenie

# Korzystając z oficjalnej dokumentacji na temat typu datetime, znajdź metodę na skonwertowanie datetime na string w formacie np. "2021.08.28 12.34.56"
# Dokumentacja: https://docs.python.org/3/library/datetime.html#datetime.datetime