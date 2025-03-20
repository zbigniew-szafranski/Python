### 🔴 Wyrażenia listowe (list comprehension)

# Bardzo często zdarza się, że w kodzie tworzysz nową listę na podstawie starej, na przykład:

names = ['plik', 'kolejny_plik']
filenames = []
for name in names:
    filename = name + '.txt'  # new_elem w jakiś sposób zależy od elem 
    filenames.append(filename)
print('filenames =', filenames)  # ==> filenames = ['plik.txt', 'kolejny_plik.txt']

# Taki kod można zapisać krócej używając składni LIST COMPREHENSION:
# [_ for _ in _]
# Taki kod można przepisać tak jak poniżej:

filenames = [name + '.txt' for name in names]
print('filenames =', filenames)  # ==> filenames = ['plik.txt', 'kolejny_plik.txt']

# Albo:

lines = [
    'pierwsze drugie slowo',
    'linie to kolejne slowa',
]
comments = []
for line in lines:
    words = line.lower().split()
    comments.append(words)
print('comments =', comments)

# Ten kod można przepisac krócej:

comments = [line.lower().split() for line in lines]
print('comments =', comments)

# Zwróć uwage, że to co jest     [ TUTAJ for _ in _ ]     musi być jedną linią i musi być też wyrażeniem.
# Nie może być to instrukcja, dlatego np. ten kod nie zadziała:

# counter = 0
# result = [counter += 1 for word in words]  # ❌ nie zadziała

# Jeśli masz kilka linii kodu, to możesz umieścić je w osobnej funkcji. Na przykład poniższy kod:

PUNCTUATIONS = '.?!'

lines = [
    'pierwsze drugie. slowo',
    'linie to kolejne slowa?',
]
comments_2 = []
for line in lines:
    line = line.lower()
    for punc in PUNCTUATIONS:
        line = line.replace(punc, ' ')
    words = line.split()
    comments_2.append(words)
print('comments_2 =', comments_2)

# Można napisać prościej:

def split_to_words(line):
    line = line.lower()
    for punc in PUNCTUATIONS:
        line = line.replace(punc, ' ')
    words = line.split()
    return words

comments_2 = [split_to_words(line) for line in lines]
print('comments_2 =', comments)

### 🔴 Ćwiczenie

# Rozwiń program z M05L16 tak, aby mając listę `elements` dla każdego jej elementu wywołać metodę .text_content() i tak uzyskane stringi zebrać w jedną, nową listę. Następnie wyświetl tą listę, każdy element w osobnej linii.