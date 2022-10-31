

class Ride_manager:
    def __init__(self):
        print('Ride Manager activated')
        self.__account = 0
        self.__trip_history = []
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

    def get_available_cars(self):
        return self.__available_cars

    def total_income(self):
        return self.__account

    def trip_history(self):
        return self.__trip_history

    def find_a_vehicle(self, rider, vehicle_type, destination):
        if vehicle_type == 'car':
            if len(self.__available_cars) == 0:
                print('Sorry! No car is available now.')
                return False
        for car in self.__available_cars:
            # print('potential', rider.location, car.driver.location)
            if abs(rider.location-car.driver.location) < 10:
                distance = abs(rider.location-destination)
                fare = distance*car.rate
                if rider.balance < fare:
                    print('Insufficient Payment. Balance: ',
                          rider.balance, ' Fare: ', fare)
                    return False
                if car.status == 'available':
                    car.status = 'unavailable'
                    trip_info = f'Found a matched for {rider.name} for Fare: ${fare} with {car.driver.name} started from {rider.location} to {destination}\n'
                    rider.start_a_trip(fare, trip_info)
                    car.driver.start_a_trip(
                        rider.location, destination, fare*0.8, trip_info)
                    self.__account += fare*0.2
                    self.__available_cars.remove(car)

                    self.__trip_history.append(trip_info)
                    print(trip_info)

                    return True


uber = Ride_manager()
