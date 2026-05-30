# Average Rainfall

# Input the years recorded
num_years = 0
while num_years < 1:
    num_years = int(input("Please enter the number of years (number must be greater than 0): "))

total_months = num_years * 12

# Get the measurements for each month in each year
total_rainfall = 0
year = 0
for num in range(num_years):    # Outer loop counting the years
    year += 1
    print("Entering rainfall for year", year)
    month = 1
    for eachPass in range(12):      # Inner loop counting the months per year
        mon_rainfall = -0.5      
        while(mon_rainfall < 0):
            print("Month", month, end=' ')
            mon_rainfall = float(input("Enter the rainfall(inches): "))
        month += 1
        total_rainfall += mon_rainfall
    print()
    

# Display the results
print("Total number of months recorded:", total_months)
print("Total inches of rainfall:", total_rainfall)
print("Average rainfall per month(inches):", round(total_rainfall / total_months, 2))




