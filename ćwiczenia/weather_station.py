# Wzorzec Observer

from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass

@dataclass
class WeatherData:
    temperature: float
    humidity: float

#Interfejs dla obserwatora
#pylint: disable=too-few-public-methods
class Observer(ABC):
    @abstractmethod
    def update(self, weather_data: WeatherData) -> None:
        pass

#Interfejs dla obiektu obserwowanego
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer)->None:
        pass

    @abstractmethod
    def detach(self, observer: Observer)->None:
        pass

    @abstractmethod
    def notify(self)->None:
        pass

class WeatherStation(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._weather_data = WeatherData(temperature=0.0, humidity=0.0)

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print(f"Odłączono obserwatora: {observer}")

    def notify(self):
        for observer in self._observers:
            observer.update(self._weather_data)

    def update_weather(self, temperature: float, humidity: float)->None:
        self._weather_data = WeatherData(temperature=temperature, humidity=humidity)
        self.notify()


class PhoneDisplay(Observer):
    def __str__(self):
        return "Wyświetlacz telefonu 📱"

    def update(self, weather_data: WeatherData):
        print(
            f"Telefon wyświetla: "
            f"Temperatura {weather_data.temperature}st.C, "
            f"Wilgotność {weather_data.humidity}"
        )

class DesktopDisplay(Observer):

    def __str__(self):
        return "Monitor komputera 🖥️"

    def update(self, weather_data: WeatherData):
        print(
            f"Monitor wyświetla: "
            f"Temperatura {weather_data.temperature}st.C, "
            f"Wilgotność {weather_data.humidity}"
        )

weather_station = WeatherStation()

phone = PhoneDisplay()
desktop = DesktopDisplay()

weather_station.attach(phone)
weather_station.attach(desktop)
weather_station.update_weather(25, 90)
