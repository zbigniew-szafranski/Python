import random

def random_numbers():
    numbers = list(range(1, 49))
    numbers_roll = random.sample(numbers, 6)
    return numbers_roll


def get_number_user():
    numbers_user = []
    while len(numbers_user)<6:
        number = int(input(f"Podaj liczbę {len(numbers_user)+1} (1-49): "))
        if number in range(1, 49) and number not in numbers_user:
            numbers_user.append(number)
        elif number in numbers_user:
            print("Ta liczba już została wybrana")
        else:
            print("Liczba jest poza zakresem 1-49")
    return numbers_user

def check_numbers(numbers_user, roll):
    if set(numbers_user) == set(roll):
        return True
    else:
        return False


def display_numbers(roll, numbers_user):
    print(f"Wylosowane liczby: {roll}")
    print(f"Twoje liczby: {numbers_user}")


def main():
    numbers_user = []
    roll = random_numbers()
    numbers_user = get_number_user()
    display_numbers(roll, numbers_user)


if __name__ == "__main__":
    main()
