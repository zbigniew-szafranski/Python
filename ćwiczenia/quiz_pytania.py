

import csv

questions = [
    ["Python jest językiem interpretowanym", "prawda"],
    ["Java i JavaScript to ten sam język programowania", "fałsz"],
    ["Lista w Pythonie może przechowywać różne typy danych", "prawda"],
    ["W Pythonie średnik na końcu linii jest obowiązkowy", "fałsz"],
    ["Funkcja print() służy do wyświetlania tekstu na ekranie", "prawda"]
]

with open('questions.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Pytanie', 'Odpowiedź'])
    writer.writerows(questions)
