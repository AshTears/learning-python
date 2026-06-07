# Exercise 5: A Complete List Program

first_list = ["pears", "books", 25, "Beyonce", 18]

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

list_option = ""
new_list = first_list.copy()

while(list_option != "quit"):
    user_value = input("Enter any value: ")
    list_option = input("add or remove? ")
    if user_value in new_list:
        if list_option.lower() == "add":
            print("That value already exists")
        else:
            new_list.remove(user_value)
    else:
        if list_option.lower() == "remove":
            print("That item cannot be removed")
        else:
            new_list.append(user_value)

