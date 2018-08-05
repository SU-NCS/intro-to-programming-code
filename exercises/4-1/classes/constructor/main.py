# write a constructor for a smart phone class
# the class must intialize properties for year, brand, price, memory, batterylife
# properties are decleare and set with "self" in the constructor
# all publically available - What does that mean
class Phone:
    def __init__(self, year,brand, price, memory, battery_life,phone_number):
        self.year = year
        self.brand = brand
        self.price = price
        self.memory = memory
        self.battery_life = battery_life
        self.phone_number = phone_number
      
        print("You now have a car with these features:")
        print("year: ", self.year)
        print("brand: ", self.brand)
        print("price: ", self.price)
        print("memory: ", self.memory)
        print("battery life: ", self.battery_life)
        print("phone number:", self.phone_number)

# function to instantiate the class
def main():
    smart_phone = Phone(2018,"Samsung", "$500", "32MB","8h","555-666-7777")
    print("Yay",smart_phone.brand)

main()
     