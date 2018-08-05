# "module" refers to code that is imported
# copy the phone class into a file called phone.py
# create 2 different objects
# charge up both their batteries
# notice that if you use the battery on one of them its doesn't affect the
# current_battery on the other other want
# Change the owner name - notice that defining the attribute(prop) outside of the
# constructor makes a "static" or shared variable

from phone import Phone  # import Phone class from phone.py

def main():
    smart_phone_1 = Phone(2018,"Samsung", "$500", "32MB","8","555-666-7777")
    smart_phone_2 = Phone(2018,"Apple", "$700", "32MB","8","444-555-666")
    # charge both phones
    smart_phone_1.charge_battery(8)
    smart_phone_2.charge_battery(8)
    # use some battery
    # use 4 hours on phone 1 and 2 hours on phone 2
    smart_phone_1.use_battery(4)
    smart_phone_2.use_battery(2)
    # test the current battery of each are different
    print("battery life is the same:",smart_phone_1.current_battery == smart_phone_2.current_battery)

    # show the owner - they are the same
    print ("owner", smart_phone_1.owner)
    print ("owner", smart_phone_2.owner)

    # change the owner on Phone - at the class level not the object
    # level and see that it changes for both
    Phone.owner = "dylan"
    print ("owner", smart_phone_1.owner)
    print ("owner", smart_phone_2.owner)

main()