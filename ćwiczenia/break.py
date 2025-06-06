# Widzę, że mamy stworzyć kilka ćwiczeń z użyciem instrukcji `break`. Co powiesz na taką zabawę - wyobraźmy sobie, że jesteś graczem w labiryncie! 🌟

print("Witaj w labiryncie! Poruszaj sie po nim używając WSAD. Wciśnij q aby zakończyć grę.")

class GameMovement:
    def __init__(self):
        self.valid_moves = ["w", "s", "a", "d"]
        self.counter = 0

    def is_valid_move(self, command):
        return command in self.valid_moves

    def print_counter(self):
        print("Poziom:", self.counter)

    def increment_counter(self):
        self.counter += 1
        self.print_counter()

def main():
    while True:
        command = input("Podaj komendę: ")
        if command == "q":
            print("Wyjście z gry")
            break
        else:
            if game_movement.is_valid_move(command):
                game_movement.increment_counter()
                print("Przesunięto się")
                continue

if __name__ == "__main__":
    game_movement = GameMovement()
    main()