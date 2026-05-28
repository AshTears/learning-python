# Income Tax Calculator

# Define user input
#gross_inc = float(input("Enter your gross income from your W-2 for 2020: "))
#num_dep = int(input("How many dependents are you claiming? "))

gross_inc = 150000
num_dep = 2

# Calculate taxable income
tax_income = gross_inc - 12200 - (2000 * num_dep)

# Calculate tax due
if tax_income <= 9875:
    tax_due = tax_income * 0.1
elif tax_income <= 40125:
    tax_due = (9875 * 0.1) + ((tax_income - 9875) * 0.12)
elif tax_income <= 85525:
    tax_due = (9875 * 0.1) + ((40125 - 9875) * 0.12) + ((tax_income - 40125) * 0.22)
elif tax_income <= 163300:
    tax_due = (9875 * 0.1) + ((40125 - 9875) * 0.12) + ((85525 - 40125) * 0.22) + ((tax_income - 85525 * 0.24))

# Print the result
print("Tax Due:", tax_due)