# "module" refers to code that is imported
# copy the phone class into a file called phone.py
# copy the main function into this file
# import the phone class code into this file
from phone import Phone  # import Phone class from phone.py

def main():
    smart_phone = Phone(2018,"Samsung", "$500", "32MB","8","555-666-7777")
    print("Yay",smart_phone.brand)
    print(str(smart_phone))
    smart_phone.charge_battery(17)
    print("current battery",smart_phone.show_current_battery(),"hours")
    smart_phone.use_battery(4)
    print("current battery",smart_phone.show_current_battery(),"hours")

main()