'''
filename: gradeTracker.py
Author: Mason Curtis
Date: 9/26/25
'''

# Needed/Used variables
studentGrades = list() # For numerical grades
studentNames = list() # For student names
passingGrade = list() # For whether they passed or not
gradeLetter = list() # For lettered grades
isAverage = list() # For telling whether or not an answer is above, below, or at the average
totalScore = 0 # Used to find the average, used to add every number from the numerical grade list to then be divided by numStudents
numStudents = int(input("Enter the number of students: "))

for i in range (1, numStudents + 1):
    name = str(input("Enter student " + str(i) + "'s name: ")) # Asks for name
    studentNames.append(name)
    grade = int(input("Enter grade for user " + str(i) + ": ")) # Asks for the grade
    studentGrades.append(grade)
    if grade >= 70: # Check for passing grade
        passingGrade.append("Passed") # passed (Had above 70)
    elif grade < 70:
        passingGrade.append("Failed") # failed (had below 70)

highestGrade = max(studentGrades) # Highest grade, find highest number in the list.
lowestGrade = min(studentGrades) # Lowest grade, finds lowest number in the list

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



# Information printed
for i in range (1, numStudents + 1):
    print(studentNames[i-1] + "\n" + str(studentGrades[i-1]) + "  " + str(gradeLetter[i-1]) + "  " + str(isAverage[i-1]))
    print(studentGrades[i-1])
    print(passingGrade[i-1])

print("Highest grade: " + str(max(studentGrades)) + "%")
print("Lowest grade: " + str(min(studentGrades)) + "%")
print("Average: " + str(average) + "%")



