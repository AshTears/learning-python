# Dictionary
my_car = {
    "brand": "Subaru",
    "model": "Impreza",
    "year": 2012,
    "color": "blue",
    "modded": False
}

keep_going = "yes"

while (keep_going != "quit"):
    user_key = input("Enter a value: ")
    options = input("update or remove: ")
    if options.lower() == "remove":
        if user_key in my_car.keys():
            my_car.pop(user_key)
            print(my_car)
        else:
            print("That is a new key.")
            user_value = input("Enter a matching value: ")
            my_car.update({user_key:user_value})
            print(my_car)
    

