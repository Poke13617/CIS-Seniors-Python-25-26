'''
filename: gradeTracker.py
Author: Mason Curtis
Date: 9/26/25
'''
import sys # this is used to force the program to end after an invalid input to restrict the program from a ZeroDivisionError.
# Needed/Used variables
studentGrades = list() # For numerical grades
studentNames = list() # For student names
passingGrade = 0 # For whether they passed or not
gradeLetter = list() # For lettered grades
isAverage = list() # For telling whether or not an answer is above, below, or at the average
totalScore = 0 # Used to find the average, used to add every number from the numerical grade list to then be divided by numStudents



# Information printing (actual)
print("=" * 40)
print("\tGrade Tracker System")
print("=" * 40)
print("Welcome to Grade Tracker!\nThis program will help you analyze student grades.\n")
numStudents = int(input("How many students are in your class? (1-20): "))
if numStudents > 20 or numStudents < 0:
    print("Error: Number must be between 1-20. The program will now terminate. Rerun the program and enter a valid number.")
    sys.exit()
print("You will enter the grades for " + str(numStudents) + " students.")
print("\n\nPlease enter student information:")
print("-" * 30)
for i in range (1, numStudents + 1):
    print("Student #" + str(i))
    name = str(input("  Enter student name: ")) # Asks for name
    studentNames.append(name)
    grade = int(input("  Enter test score (0-100): ")) # Asks for the grade
    if grade < 0 or grade > 100:
        print("Error: Grade must be between 0 and 100. Terminating program. Rerun the program and enter a valid number to continue")
        sys.exit()
    studentGrades.append(grade)
    if grade >= 70: # Check for passing grade
        passingGrade += 1 # passed (Had above 70)
    elif grade < 70:
        passingGrade += 0 # failed (had below 70)
    print("\n")
passPercent = passingGrade/numStudents
# Grade letters (A, B, C, D, F)
for i in range (1, numStudents + 1):
    if studentGrades[i-1] > 89:
        gradeLetter.append("A")
    elif studentGrades[i-1] > 79:
        gradeLetter.append("B")
    elif studentGrades[i-1] > 69:
        gradeLetter.append("C")
    elif studentGrades[i-1] > 59:
        gradeLetter.append("D")
    else:
        gradeLetter.append("F")
    totalScore = totalScore + studentGrades[i-1]
average = totalScore/numStudents

# Average or not average?
for i in range(1, numStudents + 1):
    if studentGrades[i-1] > average:
        isAverage.append("Above average")
    elif studentGrades[i-1] == average:
        isAverage.append("Average")
    elif studentGrades[i-1] < average:
        isAverage.append("Below average")

print("\n")
print("=" * 40)
print("\tGRADE ANALYSIS RESULTS")
print("=" * 40)
print("Class Summary:")
print("  Total students: " + str(numStudents)) # number of students
print("  Total Points: " + str(totalScore))  # total points (average * 10)
print("  Class average: " + str(average) + "%")# Class average
print("  Highest grade: " + str(max(studentGrades)) + "%") # Highest Score:
print("  Lowest grade: " + str(min(studentGrades)) + "%") # Lowest Score:
print("  Students passing (>=70%): " + str(passingGrade) + "/" + str(numStudents)) # Students passing (above or below 70%): #/#
print("  Pass Rate: " + str(float(passPercent * 100)) + "%")# Pass rate

print("\nGrade Distrubution") # Grade distribution
# A (90-100%)  (tip: count how many have the desired letter in the gradeLetters list)
targetChar = "A"
checkA = gradeLetter.count(targetChar)
print("  A grades (90-100%): " + str(checkA))
# B (80-89%)
targetChar2 = "B"
checkB = gradeLetter.count(targetChar2)
print("  B grades (80-89%): " + str(checkB))
# C (70-79%)
targetChar3 = "C"
checkC = gradeLetter.count(targetChar3)
print("  C grades (70-79%): "+ str(checkC))
# D (60-69%)
targetChar4 = "D"
checkD = gradeLetter.count(targetChar4)
print("  D grades (60-69%): " + str(checkD))

# F (0-59%)
targetChar5 = "F"
checkF = gradeLetter.count(targetChar5)
print("  F grades (0-59%): " + str(checkF))

# Individual student results:
print("\n\nINDIVIDUAL STUDENT RESULTS: ")
print("-" * 40)
for i in range(1, numStudents+1):
    print(studentNames[i-1] + ": " + str(float(studentGrades[i-1])) + "% (" + gradeLetter[i-1] + ") - " + isAverage[i-1])

print("\nThank you for using Grade Tracker!")