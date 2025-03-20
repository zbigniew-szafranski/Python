### 🔴 Proś o wybaczenie, nie o pozwolenie!

# Wiele operacji można wykonać na jeden z dwóch sposobów:

# 1. Poproś o pozwolenie, a następnie to wykonaj - tzw. ASK FOR PERMISSION, niezalecany ❌
# 2. Zrób to, a jeśli coś pójdzie nie tak, poproś o wybaczenie - tzw. ASK FOR FOREGIVENESS, rekomendowany ✅

# Na przykład, kalkulator pozwalający na dzielenie liczb można napisać pierwszym podejściem w ten sposób
# (❌ niezalecane):

first = 10
second = 0
if second == 0:
    result = 'błąd'
else:
    result = first / second
print('Result:', result)  # ==> 'błąd'

# Natomiast drugim podejściem wygląda to następująco
# (✅ dobrze):

first = 10
second = 0
try:
    result = first / second
except ZeroDivisionError:
    result = 'błąd'
print('Result:', result)

# W Pythonie zdecydowanie preferowane jest to DRUGIE podejście.

### 🔴 Argument za ASK FOR FOREGIVENESS.

# ❌ niezalecane podejście

args = ['pierwszy', 'drugi', 'opcjonalny trzeci']
if len(args) > 3:  # (!)
    third = args[2]
else:
    third = ''
print('third =', third)

# W tym podejściu bardzo łatwo jest wprowadzić bug (= defekt), tak jak chociażby powyżej.
# Bardzo łatwo będzie też go wprowadzić, gdy w przyszłości trzeba będzie zmienić index na inny - bo kod trzeba zaktualizować w dwóch miejscach.

# ✅ dobre podejście

args = ['pierwszy', 'drugi', 'opcjonalny trzeci']
try:
    third = args[2]
except IndexError:
    third = ''
print('third =', third)

### 🔴 Ćwiczenie

# Przepisz poniższy kod tak, aby używał podejścia ask for foregiveness zamiast ask for permission.

# (1)

words = ['ala', 'ma', 'kota', 'ala']
counter = {}
for word in words:
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] += 1
print(counter)

# (2)

words = ['ala', 'ma', 'kota', 'ala']
counter = {}
for word in words:
    if word not in counter:
        old = 0
    else:
        old = counter[word]
    counter[word] = old + 1
print(counter)