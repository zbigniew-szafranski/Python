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
    
class Skeleton(Creature):
    def __init__(self,name = "Skeleton", health=100, attack_power = 15, bow_strength = 15):
        super().__init__(name, health, attack_power)
        self.bow_strength = bow_strength
        self.add_ability("Strzał precyzyjny")
        self.add_ability("Grad strzał")
        self.add_ability("Unik")

    def attack(self):
        super_bow = super().attack()
        return super_bow + self.bow_strength

    def special_stats(self):
        print(f"Siła łuku: {self.bow_strength}")


class Zombie(Creature):
    def __init__(self,name = "Zombie", health=150, attack_power=10, super_health=50):
        super().__init__(name, health, attack_power)
        self.super_health = super_health
        self.add_ability("Wskrzeszenie")
        self.add_ability("Zarażenie")
        self.add_ability("Regeneracja")

    def attack(self):
        super_health = super().attack()
        return super_health + self.super_health

    def special_stats(self):
        print(f"Wzmocnione zdrowie: {self.super_health}")


class Goblin(Creature):
    def __init__(self, name="Goblin", health=100, attack_power=10, thief=40):
        super().__init__(name, health, attack_power)
        self.thief = thief
        self.add_ability("Kradzież kieszonkowa")
        self.add_ability("Ukrycie się")
        self.add_ability("Szybki sprint")


    def attack(self):
        super_thief = super().attack()
        return super_thief + self.thief

    def special_stats(self):
        print(f"Zdolność kradzieży: {self.thief}")


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


monsters = []
for monster_type in ["skeleton", "nieznany_potwor", "zombie", "goblin"]:
    try:
        monster = MonsterFactory.create_monster(monster_type)
        monsters.append(monster)
    except ValueError as e:
        print(f"Błąd: {e}")
        print("Pomijam tworzenie tego potwora...")
        continue

# Wyświetlamy informacje o wszystkich stworzonych potworach
for monster in monsters:
    monster.information()