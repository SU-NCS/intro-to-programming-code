# define Car template
class Car:
    def __init__(self, year, make, model, color, max_speed):
        self.__year = year
        self.__make = make
        self.__model = year
        self.__color = color
        self.__max_speed = max_speed
        self.__current_speed = 0
        print("You now have a car with these features:")
        print("year: ", self.__year)
        print("make: ", self.__make)
        print("model: ", self.__model)
        print("color: ", self.__color)
        print("max_speed: ", self.__max_speed)
        print("current speed: ", self.__current_speed)

    def start(self):
        print('Car starting')

    def stop(self):
        print('Car stopping')

    def move_forward(self):
        print('Moving forward')

    def move_reverse(self):
        print('Moving in reverse')

    def set_speed(self, speed):
        self.__current_speed = speed
        print('Moving at this speed now:', self.__current_speed)

    def brake(self):
        if self.__current_speed > 0:
            self.__current_speed = self.__current_speed - 1

    def park(self):
        print('Parking')

    def get_speed(self):
        return self.__current_speed

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
