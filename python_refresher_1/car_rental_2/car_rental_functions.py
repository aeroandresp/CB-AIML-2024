# Functions and Classes for Car Rental Platform

import datetime


class Car:
    # Variable/Class attribute to track the number of available cars
    num_cars = 0

    # Constructor
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        Car.num_cars += 1

    def print_car_info(self):
        print('Car Information:')
        print('Make: ', self.make)
        print('Model: ', self.model)
        print('Year: ', self.year)
        print('Color: ', self.color)

    # Method to Number of Available Cars
    def available_cars(self):
        print('There are currently ', Car.num_cars, 'cars available')
