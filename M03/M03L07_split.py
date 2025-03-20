### 🔴 Jak jeszcze można stworzyć listę? O pracy na stringach

content = '1234 9878\n5678 3456'
numbers = content.split()  # .split() dzieli po dowolnych białych znakach, zarówno po spacjach, znakach tabulacji jak i znakach nowych linii
print('numbers =', numbers)
print('type(numbers) =', type(numbers))
# numbers jest listą string'ów, nie int'ów!

### 🔴 Ćwiczenie

# Napisz program, który wczytuje listę wydatków z pliku expenses.txt (plik zawiera same wielkości wydatków jako liczby), a następnie wyświetla ich sumę.