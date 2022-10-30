import hashlib
from random import randint
from brta import BRTA
from vehicles import Car, Bike, Cng
from ride_manager import uber


license_authority = BRTA()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypt = hashlib.md5(password.encode()).hexdigest()
        exists = False
        with open('users.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if self.email in line:
                    exists = True
        f.close()

        if not exists:
            with open('users.txt', 'a') as file:
                file.write(f'{email} {pwd_encrypt} ')
            file.close()
        print(self.name, 'User is created')

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    line_list = line.split(' ')
                    for i, val in enumerate(line_list):
                        if email == val:
                            stored_password = line_list[i+1]
                            break
                    # stored_password = line.split(' ')[1]
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
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_a_trip(self, destination):
        pass

    def start_a_trip(self, fare):
        self.balance -= fare


class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earnings = 0
        super().__init__(name, email, password)

    def give_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            print('Sorry! You have failed. Try again')
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_no, rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type, license_no, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type, license_no, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'cng':
                new_vehicle = Cng(vehicle_type, license_no, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
        else:
            print('You not a valid driver')

    def start_a_trip(self, destination, fare):
        self.location = destination
        self.earnings += fare


rider1 = Rider('Rider1', 'rider1@gmail.com', 'rider1', randint(0, 50), 5000)

rider2 = Rider('Rider2', 'rider2@gmail.com', 'rider2', randint(0, 50), 5000)
rider3 = Rider('Rider3', 'rider3@gmail.com', 'rider3', randint(0, 50), 5000)
# rider1.log_in(email='rider1@gmail.com', password='rider1')
# rider2.log_in(email='rider2@gmail.com', password='rider2')
driver1 = Driver('driver1', 'driver1@gmail.com',
                 'driver1', randint(0, 50), 5656)
driver1.give_driving_test()
driver1.register_a_vehicle('car', 1245, 10)

driver2 = Driver('driver2', 'driver2@gmail.com',
                 'driver2', randint(0, 50), 5656)
driver2.give_driving_test()
driver2.register_a_vehicle('car', 11245, 10)

driver3 = Driver('driver3', 'driver3@gmail.com',
                 'driver3', randint(0, 50), 5656)
driver3.give_driving_test()
driver3.register_a_vehicle('car', 12245, 10)

driver4 = Driver('driver4', 'driver4@gmail.com',
                 'driver4', randint(0, 50), 5656)
driver4.give_driving_test()
driver4.register_a_vehicle('car', 12445, 10)

print(uber.get_available_cars())
uber.find_a_vehicle(rider1, 'car', 90)
