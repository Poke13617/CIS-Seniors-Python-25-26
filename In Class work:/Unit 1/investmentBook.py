'''
Program: investmentBook.py
Author: Mason Curtis
Class: CIS Seniors
Date: 9/22/25
Compute an investment report
1. The inputs are:
    starting investment amount
    number of years
    Interest rate (an integer percent)

    2. The report is displayed in tabular form with a header
    3. Computations and outputs:
        for each year of the investment
            compute the interest and add it to the investment
            print a formatted row of results for that year
    4. The ending investment and interest you have paid in total are also displayed
'''
print("=" * 40)
print("\n\nMy investment tracker")
print("=" * 40)
# Accept the inputs
startBalance = float(input("Enter the investment amount"))
years = int(input(""))
rate = int(input("Enter the rate as a percent"))

# Convert the rate to a decimal number
rate = rate/100

# Initialize the accumulator for the interest
totalInterest = 0.0

#Display the header for the table

print("%4s%18s%10s%16s" % "Year", "Starting Balance", "Interest", "Ending Balance")

# Compute and display results for each year


#Display the totals for the period