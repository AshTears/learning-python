# Exercise 5: A Complete List Program

first_list = ["pears", "books", "25", "Beyonce", "18"]

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

new_list = first_list.copy()
new_items= []

keep_going = "yes"      # Sentinel value to prevent an infinite loop

# Loop to get new values to add or remove from first_list
while(keep_going != "quit"):
    user_value = input("Enter any value: ")
    list_option = input("add or remove? ")
    if list_option.lower() == "add":
        if user_value in new_list:       
            print("That value already exists")
        else:
            new_list.append(user_value)
            new_items.append(user_value)
            print(new_list)
    else:
        if user_value in new_list:
            new_items.append(user_value)
            new_list.remove(user_value)
            print(new_list)          
        else:
            print("That item cannot be removed")                    
    keep_going = input("Do you want to continue? yes or quit: ")

# Display results
print("Original list:", first_list)
print("Items added or removed from the list:",new_items)
print("Updated list:", new_list)
print(f"Have a good day {first_name} {last_name}")

