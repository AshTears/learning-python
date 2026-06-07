# Written by Ashika Shallow on 2026-06-03
# Last edited on 2026-06-03

pversion = 1.1
bname = "Bank of Money"
isLogged = False

# print("Hello, welcome to " + bname)
# print("You are using the banking portal version " + pversion)
# print("In this portal, you can handle all your banking needs.")
# print("Please enter a selection from the following menu")
# print("Type Login to log in")
# print("Type Quit to quit")
# selection = input("Enter Login or Quit: ")
# print("You have selected " + selection)

# Working with Data Types
acctBal = 13445
locBal = 16000
savBal = 4000
savInterest = 0.025
locInterest = 0.098
months = 12
years = 8.5

# compInt = savBal * ((1 + (savInterest/months)) ** (months*years))
# print(round(compInt, 2))
# result1 = (acctBal + savBal) - locBal
# print(result1)
# result2 = (acctBal - locBal) * locInterest
# print(round(result2, 2))
# result3 = ((savInterest/months)+1)**(months*years)
# print(round(result3, 3))
# result4 = ((locInterest*months*years)+1)*locBal
# print(round(result4,2))

# List
customer_details = ["Ava McDougle", "ava@email.com", "123-456-7890"]
name = customer_details[0]
print(name)
email = customer_details[1]
print(email)
phonenumber = customer_details[2]
print(phonenumber)

transactions = [
    "1AB23456C0011523D,+$25.00",
    "1AB23456C5541225D,-$56.00",
    "1AB23456C8613005D,-$393.00",
    "1AB23456C3542215D,+$544.23",
    "1AB23456C0145125D,-$5.55",
    "1AB23456C3485125D,-$8.76"
]

print("Last transaction: " + transactions[-1])
print("2nd from the last transaction: " + transactions[-2])
print("3rd from last transaction: " + transactions[-3])