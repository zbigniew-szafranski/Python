### 🔴 Zgłaszanie błędów

# Do tej pory OBSŁUGIWALIŚMY błędy przy pomocy instrukcji try-except. Tym razem przyjrzymy się, jak my możemy ZGŁASZAĆ błędy.
# Robiliśmy to już w M04 przy pomocy sys.exit -- ale użycie tej funkcji powodowało natychmiastowe zakończenie programu, bez możliwości obsługi błędu.
# Tym razem poznasz instrukcję raise, która zgłasza błąd:

# raise ValueError("asdf")
# raise ValueError  # ✅ można bez nawiasów

# Taki błąd można normalnie obsłużyć instrukcją try-except:

description = ''
try:
    if description == "":
        raise ValueError("Opis nie może być pusty")
except ValueError:
    print("Nie można stworzyć zadania - pusty opis")

# Przy czym w praktyce najczęściej try-except znajduje się zupełnie gdzie indziej niż raise, inaczej moglibyśmy się ograniczyć do sprawdzania rezultatu if'em:

import csv

def validate_row(row):
    if 'id' not in row:
        raise ValueError("Missing id column")
    if row['id'] == '':
        raise ValueError('Missing id value')

def read_file():
    rows = []
    with open('M07/file.csv') as stream:
        reader = csv.DictReader(stream)
        for row in reader:
            validate_row(row)
            rows.append(row)
    return rows

try:
    read_file()
except ValueError as e:
    print(f"Błąd: {e.args[0]}")


### 🔴 Ćwiczenie

# Rozwiń poprzednie ćwiczenie tak, aby nie można było stworzyć TodoItem z pustym opisem (description). W którym miejscu sprawdzisz, czy mamy niepusty opis? W którym miejscu złapiesz wyjątek?