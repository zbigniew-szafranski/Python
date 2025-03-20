### 🔴 Adnotacje Dict

# W poprzedniej lekcji poznałæś tzw. typ parametryczny, jakim jest List[X].

# Podobnie jest ze słownikami - dobrze będzie określić, jakiego typu są klucze i jakiego typu są wartości. W tym celu używamy Dict[Key, Value]:

from typing import Dict, List

def count_words(words: List[str]) -> Dict[str, int]:
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter

print(count_words(['a', 'b', 'c', 'a']))

# Jeśli jednak słownik reprezentuje pewien obiekt, wówczas klucze są stringami, ale wartości mogą być różnego typu, np.:

expense = {
    'amount': 6.50,
    'description': "Ziemniaki",
}

# Jak opisać taki słownik? Użyjemy typing.Any, który oznacza dowolny typ.

from typing import Any

def process_expense(expense: Dict[str, Any]):
    print(expense)

### 🔴 Ćwiczenie

# Uzupełnij kod z poprzedniego ćwiczenia tak, aby uzupełnić brakujące adnotacje typów dotyczące samego słownika.