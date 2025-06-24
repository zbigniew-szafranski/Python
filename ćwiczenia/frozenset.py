vowels = ('a', 'e', 'i', 'o', 'u', 'y', '')

frs = frozenset(vowels)
print(frs)

person = {'name': 'John', 'sex': 'male', 'age': 25}
frs_person = frozenset(person)
print(frs_person)
