
# 👉 Obiekty to rzeczy leżące na stole - zalaminowane kartki, długopisy, pudełka czy... koty. 
# 👉 Z kolei zmienne to karteczki samoprzylepne, które naklejasz na te obiekty.
# 👉 W poniższym przykładzie na stole leży JEDEN kot, a na nim naklejone są dwie karteczki samoprzylepne, na których jest napisane mruczek oraz filemon.
# 👉 Zmienne NIE są obiektami - zmienne wskazują na obiekty.
mruczek = "kot"
filemon = mruczek

# Tak, mruczek i filemon to jeden i ten sam obiekt. To po prostu dwie różne nazwy na ten sam obiekt.
print(mruczek)
print(filemon)
print(id(mruczek))  # id(x) zwraca adres w pamięci, gdzie przechowywany jest dany obiekt. Jest to liczba reprezentująca położenie na naszym stole.
print(id(filemon))
# id mruczka i filemona jest dokładnie takie samo. Innymi słowy, oba obiekty leżą w tym samym miejscu na stole. Więc to musi być ten sam obiekt!

# Czy to znaczy, że jeśli urwę nogę filemonowi, to mruczek również będzie mieć urwaną nogę???
# Na szczęście nie - obiekty typu str, int oraz float są NIEMUTOWALNE (= niemodyfikowalne) - raz stworzone na zawsze pozostaną takie same.
mruczek[0] = "a"  # ==> TypeError: 'str' object does not support item assignment

# Można co najwyżej stworzyć nowego stringa na podstawie istniejącego.

### 🔴 Ćwiczenie: Popraw kod

currency = "usd"
currency.upper()
print("Waluta wielkimi literami:", currency)