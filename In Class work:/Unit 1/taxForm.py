'''
filename: taxForm.py
Author: Mason Curtis
Class: CIS Seniors
Date: 9/22/25

Compute a Person's income tax.
1. Significant constants
    tax rate
    standard deduction
    deduction per dependent

2. The inputs are
    gross income
    number of dependents

3. Computations:
    taxable income = gross income - the standard deduction - a deducion for each dependent
    income tax = A fixed percentage of taxable income

4. The outputs are:
    The income tax
'''

print("\n\nMy Tax Rate Calculator.")
print("=" * 40)
# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.00
DEPENDENT_DEDUCTION = 3000.00

# Request the inputs

grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome - TAX_RATE

# Display the income tax
print("The income tax is $" + str(incomeTax) + "\n\n")
