# Functions and Classes for Car Rental Platform

import datetime


class Car:
    # Variable/Class attribute to track the number of available cars
    num_cars = 0

    # cars = []
    #car_id = 0

    # Constructor
    def __init__(self, make, model, year, color, hourly=30, daily=200, weekly=1000):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.hourly = hourly
        self.daily = daily
        self.weekly = weekly
        # Car.cars = {Car.num_cars: [make, model, year, color]}
        # Car.cars.append(Car)
        Car.num_cars += 1

    # Display Car Information Method
    def print_car_info(self):
        print('Car Information:')
        print('Make: ', self.make)
        print('Model: ', self.model)
        print('Year: ', self.year)
        print('Color: ', self.color)

    # Method to Number of Available Cars
    def available_cars(self):
        print('There are currently ', Car.num_cars, 'cars available:')
        # Work in Progress
        # for i in range(Car.num_cars):
        #     print(Car.cars[i])

    # def rent_hourly(self):
