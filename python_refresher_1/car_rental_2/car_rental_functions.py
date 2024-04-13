# Functions and Classes for Car Rental Platform

# Adds classes to manipulate dates and time
from datetime import datetime

class Car:
    # Variable (Class Attribute) to track the number of available cars
    num_cars = 0

    # List (Class Attribute) to Track List of Cars
    car_list = []

    # Constructor
    def __init__(self, make, model, year, color, hourly=30, daily=200, weekly=1000):
        ### Car Attributes ###
        self.make = make
        self.model = model
        self.year = year
        self.color = color

        ### Car Rates ###
        self.hourly = hourly
        self.daily = daily
        self.weekly = weekly

        ### Car Availability ###
        self.available = True

        ### Other Attributes ###
        Car.car_list.append(self)
        Car.num_cars += 1

    # Display Car Information Method
    def print_car_info(self):
        print('Car Information:')
        print('Make:      ', self.make)
        print('Model:     ', self.model)
        print('Year:      ', self.year)
        print('Color:     ', self.color)
        print('Available: ', self.available)

    # Method to Display Number of Available Cars
    def available_cars(self):
        print('There are currently', Car.num_cars, 'cars available:')
        for i, car_obj in enumerate(Car.car_list):
            if car_obj.available:
                print(i, '--->', car_obj.year, car_obj.color, car_obj.make, car_obj.model)

    # # Method to Calculate Car Rental Bill from Hourly Rate
    # def rent_hourly(self, hours):
    #     return hours * self.hourly
    #
    # # Method to Calculate Car Rental Bill from Daily Rate
    # def rent_daily(self, days):
    #     return days * self.daily
    #
    # # Method to Calculate Car Rental Bill from Weekly Rate
    # def rent_weekly(self, weeks):
    #     return weeks * self.weekly

class Customer(Car):

    def __init__(self, name):
        self.name = name
        self.rented_cars = [] # Car objects rented by customer
        self.requested_cars = [] # Car object indices of rented cars by customer
        self.bill = 0

        ### Variables to Track Rental Time ###
        self.rental_time = 0
        self.rental_start = 0
        self.rental_end = 0

        ### Rental Modes ###
        self.hour = False
        self.day = False
        self.week = False

    # Method to Display Customer Info
    def print_customer_info(self):
        print(self.name)

    # Method for Customer to retrieve cars for rent
    def retrieve_cars(self):

        # Do if requested cars (n) is both positive and less than or equal to total available cars
        while True:
            n = int(input("Enter number of cars you would like to request: "))
            if Car.num_cars >= n > 0:
                break
            else:
                print('Error: Only', Car.num_cars, 'available to check out. Please try again')

        # Adds Customer Requested Cars into a List Based on Availability
        for i in range(0, n):
            # Infinite While Loop incase Customer Tries to Choose Unavailable Car
            while True:
                print(i+1, ':', sep='', end=' ')
                car_i = int(input('Which car would you like to rent?  '))

                if Car.car_list[car_i].available:
                    # adding the element
                    self.requested_cars.append(car_i)
                    Car.car_list[car_i].available = False
                    Car.num_cars -= 1
                    break
                else:
                    # Error Message Displayed if Customer Tries to Request an Unavailable Car
                    print('Error: Car not available. Please try again')

        print('Requested the following cars:')
        for i in self.requested_cars:
            self.rented_cars.append(Car.car_list[i])
            print(Car.car_list[i].year, Car.car_list[i].color, Car.car_list[i].make, Car.car_list[i].model)
        print('Adding Cars to ', self.name, '\'s Cart', sep='')

        # Record Start Time
        self.rental_start = datetime.now()
        print('Start of Rental:', self.rental_start)

    def rental_mode(self):
        while True:
            print('Available Rental Modes:')
            print('H or h ---> Hourly')
            print('D or d ---> Daily')
            print('W or w ---> Weekly')
            rent_method = str(input('Enter Rental Method You Desire: '))
            if rent_method == 'h' or rent_method == 'H':
                self.hour = True
                print('Rental Method: Hourly')
                break
            elif rent_method == 'd' or rent_method == 'D':
                self.day = True
                print('Rental Method: Daily')
                break
            elif rent_method == 'w' or rent_method == 'W':
                self.week = True
                print('Rental Method: Weekly')
                break
            else:
                print('Error: Not a valid rental method. Please try again')

    def return_cars(self):
        if len(self.rented_cars) != 0:
            print('Returning the following cars:')
            for i in self.requested_cars:
                Car.car_list[i].available = True
                Car.num_cars += 1
                print(Car.car_list[i].year, Car.car_list[i].color, Car.car_list[i].make, Car.car_list[i].model)
            self.rented_cars.clear()
        else:
            print('Error: You have no cars rented out')