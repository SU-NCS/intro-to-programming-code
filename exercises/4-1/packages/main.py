# "package" refers to code that is in a folder
# tell the python system that the folder is a package by adding the __init__.py file
# import by specifying the <folder>.<file>
# this helps with name spacing
import my_package.phone

def main():
    smart_phone = my_package.phone.Phone(2018,"Samsung", "$500", "32MB","8","555-666-7777")
    print("Yay",smart_phone.brand)
    print(str(smart_phone))
    smart_phone.charge_battery(17)
    print("current battery",smart_phone.show_current_battery(),"hours")
    smart_phone.use_battery(4)
    print("current battery",smart_phone.show_current_battery(),"hours")

main()