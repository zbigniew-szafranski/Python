from dataclasses import dataclass
import csv

class Creature:
    def __init__(self, name, health, attack_power):
        self.health = health
        self.attack_power = attack_power
        self.name = name
        self.abilities = []

    def add_ability(self, ability):
        self.abilities.append(ability)
        
    def attack(self):
        return self.attack_power

    def print_separate(self):
        print("--------------------------")

    def special_stats(self):
        pass

    def get_special_stat(self):
        return None, 0

    def information(self):
        self.print_separate()
        print(f"Nazwa: {self.name}")
        print(f"Zdrowie: {self.health}")
        print(f"Siła ataku: {self.attack_power}")
        if self.abilities:
            print("Specjalne umiejętności:")
            for ability in self.abilities:
                print(f"- {ability}")
        self.special_stats()
        self.print_separate()

    def save_to_csv(self):
        with open('creatures.csv', "a") as writer:
            csv_writer = csv.writer(writer)

            if writer.tell() == 0:
                csv_writer.writerow(['name', 'health', 'attack_power', 'abilities', 'special_stat'])

            stat_name, stat_value = self.get_special_stat()

            csv_writer.writerow([
                self.name,
                self.health,
                self.attack_power,
                self.abilities,
                stat_name,
                stat_value
            ])

@dataclass()
class Skeleton(Creature):
    bow_strength: int = 15
    name: str = "Skeleton"
    health: int = 100
    attack_power: int = 15

    def __post_init__(self):
        super().__init__(self.name, self.health, self.attack_power)
        self.abilities = []
        self.add_ability("Strzał precyzyjny")
        self.add_ability("Grad strzał")
        self.add_ability("Unik")

    def attack(self):
        super_bow = super().attack()
        return super_bow + self.bow_strength

    def special_stats(self):
        print(f"Siła łuku: {self.bow_strength}")

    def get_special_stat(self):
        return "bow_strength", self.bow_strength

@dataclass()
class Zombie(Creature):
    name: str = "Zombie"
    health: int =150
    attack_power: int =10
    super_health: int =50

    def __post_init__(self):
        super().__init__(self.name, self.health, self.attack_power)
        self.abilities = []
        self.add_ability("Wskrzeszenie")
        self.add_ability("Zarażenie")
        self.add_ability("Regeneracja")

    def attack(self):
        super_health = super().attack()
        return super_health + self.super_health

    def special_stats(self):
        print(f"Wzmocnione zdrowie: {self.super_health}")

    def get_special_stat(self):
        return "Wzmocnione zdrowie", self.super_health

@dataclass()
class Goblin(Creature):
    name: str ="Goblin"
    health: int =100
    attack_power: int=10
    thief: int=40

    def __post_init__(self):
        super().__init__(self.name, self.health, self.attack_power)
        self.abilities = []
        self.add_ability("Kradzież kieszonkowa")
        self.add_ability("Ukrycie się")
        self.add_ability("Szybki sprint")


    def attack(self):
        super_thief = super().attack()
        return super_thief + self.thief

    def special_stats(self):
        print(f"Zdolność kradzieży: {self.thief}")
    def get_special_stat(self):
        return "Szybka kradzież", self.thief


class MonsterFactory:
    @staticmethod
    def create_monster(monster_type: str):
        if monster_type.lower() == "skeleton":
            return Skeleton()
        elif monster_type.lower() == "zombie":
            return Zombie()
        elif monster_type.lower() == "goblin":
            return Goblin()
        else:
            raise ValueError(f"Nieznany typ potwora >>>{monster_type}<<<")


def main():
    skeleton = Skeleton()
    zombie = Zombie()
    goblin = Goblin()

    monsters = [skeleton, zombie, goblin]

    for monster in monsters:
        monster.information()
        monster.save_to_csv()

if __name__ == "__main__":
    main()

