# Zaimplementuj klasę bazową o nazwie Vehicle z metodami start() i stop(), które wypisują odpowiednio komunikaty "Pojazd rusza" oraz "Pojazd zatrzymuje się". Następnie, wykorzystując zdobytą wiedzę z przeczytanych materiałów, utwórz klasę pochodną Car, która dziedziczy po klasie Vehicle i przeciąża metodę start(), dodając do niej komunikat o uruchomieniu silnika. Użyj metody super() do wywołania metody start() klasy bazowej wewnątrz przeciążonej metody.
# Dodatkowo, zaimplementuj w klasie Car dekorator @staticmethod dla metody information(), która wypisuje statyczny komunikat podstawowych informacji o samochodzie. Przedstaw też, jak można utworzyć generator travel_miles(), który będzie iteracyjnie zwracał kolejne mile podróży samochodu, oraz zaimplementuj iterator dla klasy Car, który pozwoli iterować przez serię komunikatów (np. statusy podróży).
# Utwórz testowy kod, który zademonstruje działanie wszystkich wymienionych aspektów Twojej implementacji.

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
    def __init__(self, engine, body, wheels, type, color, HP):
        super().__init__(engine, body, wheels)
        self.type = type
        self.color = color
        self.HP = HP
        self._status_index = 0
        self._travel_statuses = [
            "Przygotowanie do podróży",
            "W trakcie jazdy",
            "Postój",
            "Koniec podróży"
        ]

    def start(self):
        print("Silnik uruchomiony")

    def stop(self):
        print("Silnik zatrzymany")

    @staticmethod
    def information():
        print("Samochód na koła, nadwozie, szyby i służy do przewożenia ludzi lub towarów")

    def travel_miles(self, max_miles):
        miles = 0
        while miles < max_miles:
            yield miles
            miles += 1
    def __iter__(self):
        self._status_index = 0
        return self

    def __next__(self):
        if self._status_index >=len(self._travel_statuses):
            raise StopIteration
        status = self._travel_statuses[self._status_index]
        self._status_index += 1
        return status

my_car = Car("gas", "sedan", 4, "sedan", "black", 100)
for status in my_car:
    print(f"Status: {status}")