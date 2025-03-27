### 🔴 Ćwiczenie

# Popraw kod z M03L09 tak, aby wczytać wydatki do listy, a następnie wylicz sumę i średnią wydatków, a także jakiej kwoty był najmniejszy i największy wydatek. Użyj wbudowanych funkcji sum, min oraz max.

EXPENSES_FILENAME = 'M03/expenses_ex.txt'
with open(EXPENSES_FILENAME) as stream:
    content = stream.read()
lines = content.split('\n')
expenses = []
for line in lines:
    token=line.split()
    if token:
        expense = float(token[0])
        expenses.append(expense)
total: float = sum(expenses)
minimum: float = min(expenses)
maximum: float = max(expenses)
avg: float = total / len(expenses)

print("Suma wydatków to: ", total)
print("Najmniejszy wydatek: ", minimum)
print("Największy wydatek: ", maximum)
print("Sredni wydatek: ", avg)