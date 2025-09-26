'''
filename: gradeTracker.py
Author: Mason Curtis
Date: 9/26/25
'''
studentGrades = list()
studentNames = list()
passingGrade = list()
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
    if grade <= 90:
        gradeLetter.append("A")
    elif grade <= 80:
        gradeLetter.append("B")
    elif grade <= 70:
        gradeLetter.append("C")
    elif grade <= 60
        gradeLetter.append("D")
for i in range (1, numStudents + 1):
    print(studentNames[i-1])
    print(studentGrades[i-1])
    print(passingGrade[i-1])
