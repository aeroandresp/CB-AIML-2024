# Main Function to Run Car Rental Platform
import car_rental_functions


def main():
    # Initialize Car Objects
    c1 = car_rental_functions.Car('Toyota', 'Camry', 2020, 'Red')
    c2 = car_rental_functions.Car('Tesla', 'Model Y', 2024, 'White')
    c3 = car_rental_functions.Car('Honda', 'Civic', 2023, 'Black')
    c4 = car_rental_functions.Car('Nissan', 'Altima', 2019, 'Blue')
    c5 = car_rental_functions.Car('Ford', 'F-150', 2022, 'Grey')

    # Customer 1
    ct1 = car_rental_functions.Customer(input('What is your name? '))
    ct1.print_customer_info()
    ct1.available_cars()
    ct1.retrieve_cars()
    ct1.rental_mode()
    ct1.available_cars()

    # Customer 1 Again
    ct1.return_cars()
    ct1.available_cars()


# Start Script Here
if __name__ == '__main__':
    main()
