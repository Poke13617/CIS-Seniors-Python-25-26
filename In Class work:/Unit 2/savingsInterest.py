'''
savings account.
'''

import math

base = float(input("Enter initial savings: "))

rate = float(input("Enter annual interest rate"))

years = int(input("Enter years that pass:"))

total = base * math.pow(1 + (rate / 100), years)

print(f"Savings after {years} years is ")