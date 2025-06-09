# Widzę, że mamy stworzyć kilka ćwiczeń z użyciem instrukcji `break`. Co powiesz na taką zabawę - wyobraźmy sobie, że jesteś graczem w labiryncie! 🌟

import tty, termios
import sys
import random
from enum import Enum

class GameState(Enum):
    PLAYING = 'playing'
    TRAPPED = 'trapped'
    WIN = 'win'
    LOSE = 'lose'

class Game:
    def __init__(self):
        self.counter = 0
        self.state = GameState.PLAYING
        self.valid_moves = ["w",
                            "s",
                            "a",
                            "d"]
        self.counter = 0
        self.score = 0
        self.treasures_points = {
            'skarb': 10,
            'piłka': 5,
            'serce': 1,
            'pułapka': -10
        }

    def find_random_treasure(self)->str:
        treasures = ["skarb",
                     "piłka",
                     "serce",
                     "pułapka"]
        return random.choice(treasures)

    def is_valid_move(self, command):
        return command in self.valid_moves

    def print_counter(self):
        print("Poziom:", self.counter)
        return

    def increment_counter(self):
        self.counter += 1
        self.print_counter()
        result = self.check_game_events()
        if result is True:
            return True
        self.counter = result
        return False


    def check_game_events(self):
        if self.counter == 5:
            fit = self.find_random_treasure()
            points = self.treasures_points[fit]
            self.score += points
            if fit == "pułapka":
                print(f"Wpadłeś w pułapkę! Tracisz {abs(points)} punktów!")
                print(f"Twój wynik to: {self.score}")
                self.state = GameState.LOSE
                return True
            else:
                print(f"Znalazłeś {fit}! Zdobywasz {points} punktów!")
                print(f"Twój wynik to: {self.score}")
                self.counter = 0
        return self.counter

    def display_game_score(self):
        print(f"\n Aktualny wynik: {self.score} punktów")

def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    print("Sterowanie: WSAD, q - wyjście")
    while True:
        command = get_char()
        if command == "q":
            print("\nWyjście z gry")
            break
        else:
            if game_movement.is_valid_move(command):
              if game_movement.increment_counter():
                  print("\nGratulacje! Koniec gry!")
                  game_movement.display_game_score()
                  break
            print("Przesunięto się")
            continue

if __name__ == "__main__":
    game_movement = Game()
    main()