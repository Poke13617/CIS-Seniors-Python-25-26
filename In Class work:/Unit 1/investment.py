'''
Program: investment.py
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

print("Investment calculator")
print("=" * 25)

# Accept the inputs
investStarter = int(input("Enter the starting amount: "))
yearsTotal = int(input("Enter the number of years: "))
interestRate = int(input("Enter the interest rate as a percent: "))

# Convert the rate to a decimal number
decIntRate = interestRate / 100

# Initialize the accumulator for the interest
i = 0
while i < int(yearsTotal):
  investStarter = investStarter * decIntRate
  print( "Year " + str(i) + "--" + str(investStarter))
  i += 1

# Display the header for the table


# Compute and display the results for each year


# Display the totals for the period

