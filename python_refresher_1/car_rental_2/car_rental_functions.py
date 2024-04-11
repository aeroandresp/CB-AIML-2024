# Functions and Classes for Car Rental Platform
class Car:
    # Variable/Class attribute to track the number of available cars
    num_cars = 0

    # Constructor
    def __init__(self, make, model, year, color, hourly=30, daily=200, weekly=1000, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.hourly = hourly
        self.daily = daily
        self.weekly = weekly
        self.available = available
        self.car_list = []
        Car.num_cars += 1

    # Display Car Information Method
    def print_car_info(self):
        print('Car Information:')
        print('Make:      ', self.make)
        print('Model:     ', self.model)
        print('Year:      ', self.year)
        print('Color:     ', self.color)
        print('Available: ', self.available)

    # Method to Add Car (class) to a List
    def add_car(self, car):
        self.car_list.append(car)

    def get_car_list(self):
        return self.car_list

    # Method to Display Number of Available Cars
    def available_cars(self, car_obj_list):
        print('There are currently', Car.num_cars, 'cars available:')
        for car_obj in car_obj_list:
            if car_obj.available:
                print(
                    car_obj.year, car_obj.color, car_obj.make, car_obj.model
                )

    # Method to Calculate Car Rental Bill from Hourly Rate
    def rent_hourly(self, hours):
        return hours * self.hourly

    # Method to Calculate Car Rental Bill from Daily Rate
    def rent_daily(self, days):
        return days * self.daily

    # Method to Calculate Car Rental Bill from Weekly Rate
    def rent_weekly(self, weeks):
        return weeks * self.weekly

class Customer(Car):

    def __init__(self, name):
        self.name = name

    def print_customer_info(self):
        print(self.name)

    # def retrive_car(self):