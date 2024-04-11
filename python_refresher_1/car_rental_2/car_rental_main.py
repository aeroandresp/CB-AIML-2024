# Main Function to Run Car Rental Platform
import car_rental_functions


def main():
    # Initialize Car Objects
    c1 = car_rental_functions.Car('Toyota', 'Camry', 2020, 'Red')
    c2 = car_rental_functions.Car('Tesla', 'Model Y', 2024, 'White')
    c3 = car_rental_functions.Car('Honda', 'Civic', 2023, 'Black')
    c4 = car_rental_functions.Car('Nissan', 'Altima', 2019, 'Blue')
    c5 = car_rental_functions.Car('Ford', 'F-150', 2022, 'Grey')

    # Add Cars to a List
    c1.add_car(c1)
    c1.add_car(c2)
    c1.add_car(c3)
    c1.add_car(c4)
    c1.add_car(c5)


    # c1.print_car_info()
    c1.available_cars()

# Start Script Here
if __name__ == '__main__':
    main()