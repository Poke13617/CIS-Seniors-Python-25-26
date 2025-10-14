'''
filename: gettingDigits.y
author: Mason Curtis
three-digit number user_vla like 927
'''

myDigit = int(input("Enter a 3 digit number: "))

ones_digit = myDigit % 10
tmp_val = myDigit // 10

tens_digit = tmp_val % 10
tmp_val = tmp_val // 10

hundreds_digit = tmp_val % 10

print("The ones place is " + str(ones_digit) + ", the tens place is " + str(tens_digit) + ", the hundreds place is " + str(hundreds_digit))