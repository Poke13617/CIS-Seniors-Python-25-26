'''
Filename: input.py
Author: Mason Curtis
Class: CIS Seniors
Date: 9/19/25
'''

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("How old are you? ")
math = input("What is Pi? ")
favorite = input("Is this your favorite class? ")

print("Your name is " + first_name + " " + last_name + ".")
print("You are " + age + " years old")

if favorite == "yes":
    favorite = "True"
    print("I am happy to hear this is your favorite class")
else:
    favorite = "False"
    print("You suck, leave!")
