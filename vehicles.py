from abc import ABC, abstractclassmethod, abstractmethod


class Vehicle(ABC):
    speed = {
        'car': 30,
        'bike': 50,
        'cng': 15
    }

    def __init__(self, vehicle_type, license_no, rate, driver) -> None:
        self.vehicle_type = vehicle_type
        self.license_no = license_no
        self.rate = rate
        self.driver = driver
        self.speed = self.speed[vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_finish(self):
        pass


class car(Vehicle):
    def __init__(self, vehicle_type, license_no, rate, driver) -> None:
        super().__init__(vehicle_type, license_no, rate, driver)

    def start_driving(self):
        print(self.vehicle_type, self.license_no, 'started')

    def trip_finish(self):
        print(self.vehicle_type, self.license_no, 'completed trip')


class Bike(Vehicle):
    def __init__(self, vehicle_type, license_no, rate, driver) -> None:
        super().__init__(vehicle_type, license_no, rate, driver)

    def start_driving(self):
        print(self.vehicle_type, self.license_no, 'started')

    def trip_finish(self):
        print(self.vehicle_type, self.license_no, 'completed trip')


class Cng(Vehicle):
    def __init__(self, vehicle_type, license_no, rate, driver) -> None:
        super().__init__(vehicle_type, license_no, rate, driver)

    def start_driving(self):
        print(self.vehicle_type, self.license_no, 'started')

    def trip_finish(self):
        print(self.vehicle_type, self.license_no, 'completed trip')
