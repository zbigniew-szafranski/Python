### 🔴 Ćwiczenie

# Przepisz poniższy kod tak, aby używał podejścia ask for foregiveness zamiast ask for permission.

words = ['ala', 'ma', 'kota', 'ala', 'kot', 'kota']
counter = {}

for word in words:
    try:
        counter[word]+=1
    except KeyError:
        counter[word] = 1
print(counter)