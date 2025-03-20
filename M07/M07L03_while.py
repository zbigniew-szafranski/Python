### 🔴 Pętla while

# Pętla while to drugi typ pętli obok pętli for.
# Pozwala na powtarzanie kodu dopóki spełniony jest pewien warunek.
# Zazwyczaj nie wiemy, ile będzie iteracji.

### 🔴 Co gdy chcemy wyświetlić zawartość pliku, ale jeśli on nie istnieje, to poczekać aż zostanie utworzony?

import time

FILENAME = 'M07/plik.txt'

def read_or_None(filename):
    try:
        with open(filename) as stream:
            content = stream.read()
            return content
    except FileNotFoundError:
        return None
    
content = read_or_None(FILENAME)
while content is None:  # poniższy kod będzie wykonywany tak długo, jak spełniony jest ten warunek
    print(f"Waiting for file {FILENAME}")
    time.sleep(1)  # odczekaj jedną sekundę
    content = read_or_None(FILENAME)
    
print("Zawartość pliku:")
print(content)

### 🔴 Ćwiczenie

# Napisz i przetestuj funkcję, która otrzymuje listę TodoItem. Każdy z nich ma pole id. Następnie funkcja sprawdza, czy jest już zadanie z id == 1, następnie id == 2 i zwraca pierwszy wolny id. Funkcja ta przyda się później do generowania nowych id.
# Napisz testy!