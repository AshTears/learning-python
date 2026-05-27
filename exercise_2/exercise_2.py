# Book Club Points

no_of_books = int(input("How many books did you buy this month: ")) # Get user input
points = 0

# Using the match statement instead of if...elif statements
match no_of_books:
    case 0:
        points = 0
    case 1:
        points = 10
    case 2:
        points = 25
    case 3:
        points = 40
    case _:
        points = 75

print("You are awarded", points, "points.")

# Extra
if points >= 75:
    print("You will receive a 10% discount on your next purchase.")
