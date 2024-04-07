#Main Function to Run Car Rental Platform
import car_rental_functions


def main():
    c1 = car_rental_functions.Car('Toyota', 'Camry', 2020, 'Red')
    c2 = car_rental_functions.Car('Tesla', 'Model Y', 2024, 'White')
    c1.print_car_info()
    c1.available_cars()
    c2.print_car_info()
    c2.available_cars()

#Start Script Here
if __name__ == '__main__':
    main()