# add methods to the class: __str__(self), how to call,  
# total price if tax is supplied
# current battery life - add to current - remove from current - show current
class Phone:
    def __init__(self, year,brand, price, memory, battery_life,phone_number):
        self.year = year
        self.brand = brand
        self.price = price
        self.memory = memory
        self.battery_life = battery_life
        self.phone_number = phone_number
        self.current_battery = 0
      
        print("You now have a car with these features:")
        print("year: ", self.year)
        print("brand: ", self.brand)
        print("price: ", self.price)
        print("memory: ", self.memory)
        print("battery life: ", self.battery_life,"hours")
        print("phone number:", self.phone_number)

    def charge_battery(self,hours):
      # can't be greater than battery_life
      if (self.current_battery + hours) <= int(self.battery_life):
        self.current_battery += hours
      else:
        self.current_battery = int(self.battery_life)
      #print("charge",self.current_battery)
    
    def use_battery(self,hours):
      # can't be negative
      #print("type",type(self.current_battery))
      if (self.current_battery - hours) >= 0:
        self.current_battery -= hours
      else:
        self.current_battery = 0
      #print("use",self.current_battery)

    def show_current_battery(self):
      return self.current_battery

    #show the string your want user to see 
    def __str__(self):
      return "year: {}, brand: {}, price: {}".format(self.year, self.brand, self.price)

    #


     