import random

def random_numbers():
    return sorted(random.sample(range(1, 50), 6))


def get_number_user():
    numbers_user = []
    while len(numbers_user)<6:
        try:
            number = int(input(f"Podaj liczbę {len(numbers_user)+1}: "))
            if 1 <= number <= 49 and number not in numbers_user and number is not str:
                numbers_user.append(number)
            elif number in numbers_user:
                print("Ta liczba już została wybrana")
            else:
                print("Liczba jest poza zakresem 1-49")
        except ValueError:
            print("Podałeś liczbę, podaj cyfre")
    return sorted(numbers_user)

def check_numbers(numbers_user, drawn):
    return len(frozenset(numbers_user) & frozenset(drawn)), frozenset(numbers_user) & frozenset(drawn)


def display_numbers(drawn, numbers_user):
    print(f"Wylosowane liczby: {','.join(map(str, drawn))}")
    print(f"Twoje liczby: {','.join(map(str, numbers_user))}")
    count, matched = check_numbers(numbers_user, drawn)
    print(f"Trafiłeś {count} liczb!")
    if matched:
        print(f"Trafione liczby to: {','.join(map(str, matched))}")
    display_funny_com(count)


def display_funny_com(count):
    match count:
        case 6:
            print("🎉 JESTEŚ MILIONEREM! 🎉")
        case 5:
            print("WOW! Niewiele brakowało do głównej wygranej! 🎯")
        case 4:
            print("Brawo! Niezły wynik! 🌟")
        case 3:
            print("Nie jest źle! 👍")
        case 2:
            print("Zawsze to coś! 😊")
        case 1:
            print("Lepszy rydz niż nic! 🎲")
        case 0:
            print("Może następnym razem się uda! 🍀")


def main():
    roll = random_numbers()
    numbers_user = get_number_user()
    display_numbers(roll, numbers_user)


if __name__ == "__main__":
    main()
