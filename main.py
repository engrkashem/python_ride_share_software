import hashlib
from random import randint
import threading
from brta import BRTA
from vehicles import Car, Bike, Cng
from ride_manager import uber


license_authority = BRTA()


class UserAlreadyExists(Exception):
    def __init__(self, email, *args: object) -> None:
        print(f'User {email} already exists.')
        super().__init__(*args)


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypt = hashlib.md5(password.encode()).hexdigest()
        exists = False
        with open('users.txt', 'r') as f:
            lines = f.read()
            # for line in lines:
            if self.email in lines:
                exists = True
                # raise UserAlreadyExists(email)
        f.close()

        if not exists:
            with open('users.txt', 'a') as file:
                file.write(f'{email} {pwd_encrypt} \n')
            file.close()
        # print(self.name, 'User is created')

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()  # lines is a list

            for line in lines:
                if email in line:
                    line_list = line.split(' ')
                    for i, val in enumerate(line_list):
                        if email == val:
                            stored_password = line_list[i+1].split('\n')[0]
                            break

        file.close()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == stored_password:
            print('Valid User')
        else:
            print('Invalid User')


class Rider(User):
    def __init__(self, name, email, password, location, balance,) -> None:
        self.location = location
        self.balance = balance
        self.__trip_history = []
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_a_trip(self, destination):
        pass

    def get_trip_history(self):
        return self.__trip_history

    def start_a_trip(self, fare, trip_info):
        print(f'A trip started for {self.name}\n')
        self.balance -= fare
        self.__trip_history.append(trip_info)


class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earnings = 0
        self.__trip_history = []
        self.vehicle = None
        super().__init__(name, email, password)

    def give_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            # print('Sorry! You have failed. Try again')
            self.license = None
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_no, rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                self.vehicle = Car(vehicle_type, license_no, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            elif vehicle_type == 'bike':
                self.vehicle = Bike(vehicle_type, license_no, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            elif vehicle_type == 'cng':
                self.vehicle = Cng(vehicle_type, license_no, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
        else:
            pass
            # print('You not a valid driver.')

    def get_trip_history(self):
        return self.__trip_history

    def start_a_trip(self, start, destination, fare, trip_info):
        self.location = destination
        self.earnings += fare
        # Start threads
        trip_thread = threading.Thread(
            target=self.vehicle.start_driving, args=(start, destination,))
        trip_thread.start()
        # self.vehicle.start_driving(start, destination)
        self.__trip_history.append(trip_info)


rider1 = Rider('Rider1', 'rider1@gmail.com', 'rider1', randint(0, 50), 1000)
rider2 = Rider('Rider2', 'rider2@gmail.com', 'rider2', randint(0, 50), 5000)
rider3 = Rider('Rider3', 'rider3@gmail.com', 'rider3', randint(0, 50), 5000)
rider4 = Rider('Rider4', 'rider4@gmail.com', 'rider4', randint(0, 50), 5000)
rider5 = Rider('Rider5', 'rider5@gmail.com', 'rider5', randint(0, 50), 5000)
# rider1.log_in(email='rider1@gmail.com', password='rider1')
# rider2.log_in(email='rider2@gmail.com', password='rider2')

for i in range(1, 100):
    driver1 = Driver(f'driver{i}', f'driver{i}@gmail.com',
                     f'driver{i}', randint(0, 100), randint(1000, 9999))
    driver1.give_driving_test()
    driver1.register_a_vehicle('car', randint(10000, 99999), 10)


# print(uber.get_available_cars())
uber.find_a_vehicle(rider1, 'car', randint(1, 100))
uber.find_a_vehicle(rider2, 'car', randint(1, 100))
uber.find_a_vehicle(rider3, 'car', randint(1, 100))
# uber.find_a_vehicle(rider4, 'car', randint(1, 100))
# uber.find_a_vehicle(rider5, 'car', randint(1, 100))


print(rider1.get_trip_history())
print(uber.total_income())
