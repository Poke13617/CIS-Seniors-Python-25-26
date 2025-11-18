"""
fitness Tracker Assignment
Program: fitnessTracker.py
Author: Mason Curtis
Date: 11/18/2025

This program is to show the user's knowledge on the main() function and how to use them. Below is fixed code to reorganize the information in order to run in the function.
"""


# UNSTRUCTURED PROGRAM - Needs fixing!
# print("Fitness Tracker")
# print("===============")
#
# exercise = input("What exercise did you do? ")
# duration_str = input("How many minutes? ")
# duration = int(duration_str)
#
# calories_per_minute = 8  # Average
# total_calories = duration * calories_per_minute
#
# print("Exercise: " + exercise)
# print("Duration: " + str(duration) + " minutes")
# print("Calories burned: " + str(total_calories))
#
# if total_calories >= 300:
#     print("Great workout!")
# else:
#     print("Good start! Try for 30+ minutes next time.")







def welcomeText():
    print("\n\nFitness Tracker")
    print("===============\n")

def get_exercise_type():
    exercise = input("What exercise did you do? ")
    return exercise


def get_duration():
    duration_str = input("How many minutes? ")

    duration = int(duration_str)
    return duration




def total_calories(duration):
    calories_per_minute = 8  # Average
    total_calories = duration * calories_per_minute
    return total_calories

def totalCalorie(total_calories):
    if total_calories >= 300:
        print("Great workout!\n")
    else:
        print("Good start! Try for 30+ minutes next time.\n")


def information(exercise, duration, calories):
    print("Exercise: " + exercise)
    print("Duration: " + str(duration) + " minutes")
    print("Calories burned: " + str(calories))


def main():


    
    exercise = get_exercise_type

    duration = get_duration


    welcomeText()

    total_cals = total_calories(duration)

    totalCalorie(total_cals)
    
    information(exercise, duration, total_cals)








    



if __name__ == "__main__":
    main()