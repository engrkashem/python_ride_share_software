

class Ride_manager:
    def __init__(self):
        print('Ride Manager activated')
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cngs = []

    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        elif vehicle_type == 'cng':
            self.__available_cngs.append(vehicle)

    def match_a_vehicle(self):
        pass


uber = Ride_manager()
