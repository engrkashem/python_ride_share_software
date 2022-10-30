from abc import ABC, abstractclassmethod, abstractmethod


class Vehicle(ABC):
    speed = {
        'car': 30,
        'bike': 50,
        'cng': 15
    }

    def __init__(self, vehicle_type, rate, driver) -> None:
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.speed = self.speed[vehicle_type]

    @abstractmethod
    def start(self):
        pass

    def move(self):
        pass
