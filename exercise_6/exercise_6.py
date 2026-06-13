# A Complete Tuple Program

my_tuple = ("Canada", "Ghana", "England", "Mexico", "Russia")

# Get some user info
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

my_list = list(my_tuple)

keep_going ="yes"              # Sentinel value to prevent an infinite loop
add_remove = []

# Loop to get new values to add or remove from first_list
while(keep_going != "quit"):
    user_value = input("Enter any value: ")
    list_option = input("add or remove? ")
    if list_option.lower() == "add":
        if user_value in my_list:       
            print("That value already exists")
        else:
            add_remove.append(user_value)
            my_list.append(user_value)
            print(my_list)
    else:
        if user_value in my_list:
            add_remove.append(user_value)
            my_list.remove(user_value)
            print(my_list)          
        else:
            print("That item cannot be removed")                    
    keep_going = input("Do you want to continue? yes or quit: ")

new_tuple = tuple(my_list)

# Display results
print("Original tuple:", my_tuple)
print("Items added or removed from the list:",add_remove)
print("Updated tuple:", new_tuple)
print(f"Have a good day {first_name} {last_name}")
