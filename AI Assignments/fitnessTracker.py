# UNSTRUCTURED PROGRAM - Needs fixing!

def welcomeText():
    print("Fitness Tracker")
    print("===============")

def total_calories(duration):
    calories_per_minute = 8  # Average
    total_calories = duration * calories_per_minute
    return total_calories

def totalCalorie(total_calories):
    if total_calories >= 300:
        print("Great workout!")
    else:
        print("Good start! Try for 30+ minutes next time.")


def information(exercise, duration, calories):
    print("Exercise: " + exercise)
    print("Duration: " + str(duration) + " minutes")
    print("Calories burned: " + str(calories))


def main():




    
    exercise = input("What exercise did you do? ")

    duration_str = input("How many minutes? ")

    duration = int(duration_str)


    welcomeText()
    total_cals = total_calories(duration)
    totalCalorie(total_cals)
    information(exercise, duration, total_cals)








    



if __name__ == "__main__":
    main()