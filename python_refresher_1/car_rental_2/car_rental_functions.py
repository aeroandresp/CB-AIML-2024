# Functions and Classes for Car Rental Platform

# Adds classes to manipulate dates and time
from datetime import datetime

class Car:
    # Variable (Class Attribute) to track the number of available cars
    num_cars = 0

    # List (Class Attribute) to Track List of Cars
    car_list = []

    # Constructor
    def __init__(self, make, model, year, color, hourly=60, daily=400, weekly=2000):
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

        ### Other ###
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

    def print_rental_modes(self):
        print('Rental Modes Available:')
        print('1 ---> Hourly')
        print('2 ---> Daily')
        print('3 ---> Weekly')
        user_input = int(input('Enter Rental Mode to See Rates of Available Cars: '))
        if user_input == 1:
            for i, car_obj in enumerate(Car.car_list):
                if car_obj.available:
                    print(i, '--->', car_obj.year, car_obj.color, car_obj.make, car_obj.model,
                          'Hourly Rate in Dollars:', car_obj.hourly)
        elif user_input == 2:
            for i, car_obj in enumerate(Car.car_list):
                if car_obj.available:
                    print(i, '--->', car_obj.year, car_obj.color, car_obj.make, car_obj.model,
                          'Daily Rate in Dollars:', car_obj.daily)
        elif user_input == 3:
            for i, car_obj in enumerate(Car.car_list):
                if car_obj.available:
                    print(i, '--->', car_obj.year, car_obj.color, car_obj.make, car_obj.model,
                          'Weekly Rate in Dollars:', car_obj.weekly)
        else:
            print('Error: Invalid Option')
            print('Returning to Main Menu\n\n')


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
        print('Start Time of Rental:', self.rental_start)

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
                print('Error: Not a valid rental mode. Please try again')

    def return_cars(self):
        if len(self.rented_cars) != 0:
            self.rental_end = datetime.now()
            self.rental_time = self.rental_end - self.rental_start
            print('Returning ', self.name, '\'s Cars', sep='')
            print('End Time of Rental:', self.rental_end)
            print('Returning the following cars:')
            for i in self.requested_cars:
                Car.car_list[i].available = True
                Car.num_cars += 1
                print(Car.car_list[i].year, Car.car_list[i].color, Car.car_list[i].make, Car.car_list[i].model)
                if self.hour:
                    conversion = 60*60 # Seconds to Minutes to Hours
                    self.bill += (self.rental_time.total_seconds()/conversion)*Car.car_list[i].hourly
                elif self.day:
                    conversion = 60 * 60 * 24 # Seconds to Minutes to Hours to Days
                    self.bill += (self.rental_time.total_seconds() / conversion) * Car.car_list[i].daily
                elif self.week:
                    conversion = 60 * 60 * 24 * 7  # Seconds to Minutes to Hours to Days to Weeks
                    self.bill += (self.rental_time.total_seconds() / conversion) * Car.car_list[i].weekly
            self.bill = round(self.bill, 2)
            self.rented_cars.clear()
            print(self.name, '\'s Total Bill: $', self.bill, sep='')
        else:
            print('Error: You have no cars rented out')