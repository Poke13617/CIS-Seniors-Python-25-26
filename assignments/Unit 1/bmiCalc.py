'''
filename: bmiCalc.py
Description:

Specific Data to Collect:

User's name
Age (integer)
Weight in pounds (float)
Height in inches (integer)
Weekly exercise hours (float)
Fitness goal (string)

'''

# Get input for the variables
name = str(input("Enter your name here: "))
age = int(input("Enter age here: "))
weight = float(input("Enter weight in pounds here: "))
height = int(input("Enter height in inches: "))
hours = float(input("Enter the number of excercise hours in a week: "))
fitGoal = str(input("Enter the fitness goal here: "))

# Get the BMI

bmi = weight/float(height) * 703
bmi = round(bmi/100, 1)
calsBurned = hours * 300
exerciseMinutes = round(hours/7, 1)
heightFt = float(height)/12
print("\n\n")
print("=" * 40)
print("Fitness progress Report For: " + name)
print("=" * 40)
print("\n\n")
print("Personal Information: ")
print("Your name: " + str(name))
print("Your age: " + str(age))
print("your weight: " + str(weight))
print("your height: " + str(height) + " inches ( " + str(heightFt) + " Feet) ")

print("\n\n")
print("BMI: " + str(bmi))
print("Weekly exercise: " + str(hours) + " hours per week")
print("Daily exercise: " + str(exerciseMinutes) + " minutes per day")
print("Estimated weekly calories burned: " + str(calsBurned) + " calories")
print("Your fitness goal was: " + fitGoal)
print("\n")
print("Great job so far!")