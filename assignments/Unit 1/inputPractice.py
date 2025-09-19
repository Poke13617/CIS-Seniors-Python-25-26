'''
Filename: inputPractice.py
Author: Mason Curtis
Class: CIS Seniors
Date: 9/19/25

Task: Ask the following questions:
First Name
Last Name
Favorite color
First Number
Second Number
Favorite TV Show
Favorite Movie
Favorite Song
Favorite Food
'''
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
favorite_color = input("Enter your favorite color: ")
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
favorite_tv_show = input("What is your favorite TV Show? ")
favorite_movie = input("What is your favorite movie? ")
favorite_song = input("What is your favorite song? ")
favorite_food = input("What is your favorite food? ")

math_one = number_one + number_two
math_two = number_one ** number_two
math_three = number_one - number_two
print("Well, " + first_name + " " + last_name + ", it says here that your favorite color is " + favorite_color + ". The numbers you inputted would equal " + str(math_one) + " if you added them together and " + str(math_two) + " if you used the second number as an exponent to the first. You would also get " + str(math_three) + " if you subtracted " + str(number_one) + " from " + str(number_two) + ". It says here that you enjoyed " + favorite_tv_show + " and " + favorite_movie  + ". I've likely never heard of them, but they sound cool! But when it comes to " + favorite_song + ", there's a chance that I've heard of that song, at least a snippet. So your favorite food is apparently " + favorite_food + ". That sounds interesting.")