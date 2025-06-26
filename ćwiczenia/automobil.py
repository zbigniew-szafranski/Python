# Zaimplementuj klasę bazową o nazwie Vehicle z metodami start() i stop(), które wypisują odpowiednio komunikaty "Pojazd rusza" oraz "Pojazd zatrzymuje się". Następnie, wykorzystując zdobytą wiedzę z przeczytanych materiałów, utwórz klasę pochodną Car, która dziedziczy po klasie Vehicle i przeciąża metodę start(), dodając do niej komunikat o uruchomieniu silnika. Użyj metody super() do wywołania metody start() klasy bazowej wewnątrz przeciążonej metody.
# Dodatkowo, zaimplementuj w klasie Car dekorator @staticmethod dla metody information(), która wypisuje statyczny komunikat podstawowych informacji o samochodzie. Przedstaw też, jak można utworzyć generator travel_miles(), który będzie iteracyjnie zwracał kolejne mile podróży samochodu, oraz zaimplementuj iterator dla klasy Car, który pozwoli iterować przez serię komunikatów (np. statusy podróży).
# Utwórz testowy kod, który zademonstruje działanie wszystkich wymienionych aspektów Twojej implementacji.
import time

class Vehicle:
    def __init__(self, engine, body, wheels):
        self.engine = engine
        self.body = body
        self.wheels = wheels


    def start(self):
        print("Pojazd rusza")
    def stop(self):
        print("Pojazd zatrzymuje się")

class Car(Vehicle):
    def __init__(self, engine, body, wheels, color, hp):
        super().__init__(engine, body, wheels)
        self.color = color
        self.hp = hp


    def start(self):
        super().start()
        print("Silnik uruchomiony")

    def stop(self):
        super().stop()
        print("Silnik zatrzymany")

    @staticmethod
    def information():
        print("Samochód na koła, nadwozie, szyby i służy do przewożenia ludzi lub towarów")


    def travel_miles(self):
        miles = 0
        while True:
            yield f"Mile {miles}"
            miles += 1


    def __iter__(self):
        self._travel_statuses = iter([
            "Przygotowanie do podróży",
            "W trakcie jazdy",
            "Postój",
            "Koniec podróży"
        ])
        return self

    def __next__(self):
        return next(self._travel_statuses)

my_car = Car("gas", "sedan", 4, "black", 100)
my_car.start()
my_car.stop()
my_car.information()

mile_gen = my_car.travel_miles()
print(next(mile_gen))
print(next(mile_gen))

for status in my_car:
    print(status)