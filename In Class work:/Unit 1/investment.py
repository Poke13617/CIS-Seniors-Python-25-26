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
print("")
# Accept the inputs
investStarter = int(input("Enter the starting amount: "))
yearsTotal = int(input("Enter the number of years: "))
interestRate = int(input("Enter the interest rate as a percent: "))
investStarter2 = investStarter

print("")
# Convert the rate to a decimal number
decIntRate = interestRate / 100

# Display the header for the table

print("=" * 40)
print("What your " + str(yearsTotal) + " year investment of $" + str(investStarter) + " looks like.")
print("=" * 40)
print("")

# Initialize the accumulator for the interest
i = 0
print("-" * 40)
print("||      Year       ||     investment   ")

while i < int(yearsTotal):
  investStarter2 = investStarter2 * (1 + decIntRate)
  print("-" * 40)
  print( "||     Year " + str(i+1) + "      ||      $" + str(round(investStarter2, 2)))
  i += 1
print("-" * 40)
print("\nAfter " + str(yearsTotal) + " Years, your investment of $" + str(investStarter) + " would turn into $" + str(round(investStarter2, 2)))
# Compute and display the results for each year (above)


# Display the totals for the period

