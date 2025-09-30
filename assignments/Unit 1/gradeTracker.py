'''
filename: gradeTracker.py
Author: Mason Curtis
Date: 9/26/25
'''
studentGrades = list()
studentNames = list()
passingGrade = list()
gradeLetter = list()
isAverage = list()
totalScore = 0
numStudents = int(input("Enter the number of students: "))

for i in range (1, numStudents + 1):
    name = str(input("Enter student " + str(i) + "'s name: "))
    studentNames.append(name)
    grade = int(input("Enter grade for user " + str(i) + ": "))
    studentGrades.append(grade)
    if grade >= 70:
        passingGrade.append("Passed")
    elif grade < 70:
        passingGrade.append("Failed")

highestGrade = max(studentGrades)
lowestGrade = min(studentGrades)

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
for i in range(1, numStudents + 1):
    if studentGrades[i-1] > average:
        isAverage.append("Above average")
    elif studentGrades[i-1] == average:
        isAverage.append("Average")
    elif studentGrades[i-1] < average:
        isAverage.append("Below average")
for i in range (1, numStudents + 1):
    print(studentNames[i-1] + "\n" + str(studentGrades[i-1]) + "  " + str(gradeLetter[i-1]) + "  " + str(isAverage[i-1]))
    print(studentGrades[i-1])
    print(passingGrade[i-1])

print("Highest grade: " + str(max(studentGrades)) + "%")
print("Lowest grade: " + str(min(studentGrades)) + "%")
print("Average: " + str(average) + "%")