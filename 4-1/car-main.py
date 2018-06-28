from car import Car
# function to instantiate the class
def main():

    year = input('Enter the car year: ')
    color = input('Enter the car color: ')
    make = input('Enter the car make: ')
    model = input('Enter the car model: ')
    max_speed = input('Enter the car\'s max speed:')

# instantiate a car
    mycar = Car(year, make, model, color, max_speed)

 # call methods on car
    mycar.start()


# call main
main()