# Napisz program symulujący quiz, który wczyta serię pytań i odpowiedzi typu prawda/fałsz z pliku 'questions.csv'. Program ma wyświetlać pytania kolejno i oczekiwać na odpowiedź użytkownika. Poprawna odpowiedź prowadzi do następnego pytania. Gdy użytkownik wpisze 'skip' pomiń pytanie, a gdy wpisze 'exit' natychmiast zakończ quiz. Nie wymagaj ponownego odpowiadania na błędne odpowiedzi; zamiast tego, przechodź do kolejnego pytania. Na zakończenie podaj liczbę poprawnych odpowiedzi uzyskaną przez użytkownika.
# Wskazówka: Wykorzystaj poznane instrukcje: 'match','break' i 'continue'.
# - Hint - `match`!
# Zastosuj instrukcję **`match`** do sprawdzania wprowadzonych przez użytkownika odpowiedzi (**`"skip"`**, **`"exit"`**).
# - Hint - `continue`!
# Aby pominąć pytanie po wpisaniu **`"skip"`**, użyj instrukcji **`continue`**, która pozwoli przejść do następnego pytania bez zwiększania licznika poprawnych odpowiedzi.
# - Hint - `break`!
#  Użyj **`break`** do natychmiastowego zakończenia quizu w przypadku wpisania przez użytkownika komendy **`"exit"`**.

import csv

with open('questions.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        question = row[0]
        answer = row[1]
        print(question)
        user_answer = input("Podaj odpowiedź: ")
        match user_answer:
            case "skip":
                continue
            case "exit":
                break
            case "prawda":
                print("Poprawna odpowiedź!")
            case "fałsz":
                print("Niepoprawna odpowiedź!")
