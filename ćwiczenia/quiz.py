# Napisz program symulujący quiz, który wczyta serię pytań i odpowiedzi typu prawda/fałsz z pliku 'questions.csv'. Program ma wyświetlać pytania kolejno i oczekiwać na odpowiedź użytkownika. Poprawna odpowiedź prowadzi do następnego pytania. Gdy użytkownik wpisze 'skip' pomiń pytanie, a gdy wpisze 'exit' natychmiast zakończ quiz. Nie wymagaj ponownego odpowiadania na błędne odpowiedzi; zamiast tego, przechodź do kolejnego pytania. Na zakończenie podaj liczbę poprawnych odpowiedzi uzyskaną przez użytkownika.
# Wskazówka: Wykorzystaj poznane instrukcje: 'match','break' i 'continue'.
# - Hint - `match`!
# Zastosuj instrukcję **`match`** do sprawdzania wprowadzonych przez użytkownika odpowiedzi (**`"skip"`**, **`"exit"`**).
# - Hint - `continue`!
# Aby pominąć pytanie po wpisaniu **`"skip"`**, użyj instrukcji **`continue`**, która pozwoli przejść do następnego pytania bez zwiększania licznika poprawnych odpowiedzi.
# - Hint - `break`!
#  Użyj **`break`** do natychmiastowego zakończenia quizu w przypadku wpisania przez użytkownika komendy **`"exit"`**.

import csv
FILE = 'questions.csv'

def load_questions(filename: str):
    questions = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            questions.append((row[0], row[1].lower()))
    return questions

def run_quiz(questions):
    correct_answers = 0
    for question, answer in questions:
        print(question)
        user_answer = input("Podaj odpowiedź(prawda/fałsz, skip/exit): ")

        match user_answer:
            case "skip":
                print("Skipping answer")
                continue
            case "exit":
                print("Zakończono quiz")
                break

        if user_answer == answer:
            correct_answers += 1
            print("Poprawna odpowiedź!")
        else:
            print(f"Nieprawidłowa odpowiedź. Prawidłowa odpowiedź to {answer}\n")
    return correct_answers

def main():
    questions = load_questions(FILE)
    correct_answers = run_quiz(questions)
    print(f"Liczba poprawnych odpowiedzi: {correct_answers} poza {len(questions)} prawidłowymi odpowiedziami")


if __name__ == "__main__":
    main()


