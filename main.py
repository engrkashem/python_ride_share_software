import hashlib
from brta import BRTA


license_authority = BRTA()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypt = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'w') as file:
            file.write(f'{email} {pwd_encrypt}')
        file.close()
        print(self.name, 'User is created')

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        file.close()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == stored_password:
            print('Valid User')
        else:
            print('Invalid User')


class Rider(User):
    def __init__(self, location, balance, name, email, password) -> None:
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
    def __init__(self, location, license, name, email, password) -> None:
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

    def start_a_trip(self, destination, fare):
        self.location = destination
        self.earnings += fare


hero = User('Hero Gadha', 'hero@nayak.com', 'herohero')
User.log_in('hero@nayak.com', 'herohero')

kuber = Driver(54, 999, 'Kuber Majhi', 'kuber@majhi.com', 'kopilajaisna',)
result = license_authority.validate_license(kuber.email, kuber.license)
print(result)
kuber.give_driving_test()
result = license_authority.validate_license(kuber.email, kuber.license)
print(result)
