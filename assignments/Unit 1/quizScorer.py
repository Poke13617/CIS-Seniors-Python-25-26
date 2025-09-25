'''
Program name: quizScorer.py
Author: Mason Curtis
Date: 9/25/25
'''
numRight = 0

problem = int()
# Get a list name
studentKey = list()
teacherKey = list()
# Ask the student's name
studentName = input("Enter student's name: ")
# Ask how many quiz questions there are
numQs = int(input("How many questions are there? " ))
# Use a for loop to ask for each answer
for numQs in range (1, numQs + 1):
    problem = int(input("Did the student answer true or false for question " + str(numQs) + "? Answer 1 for true or 0 for false. "))
    if problem == 0:
        studentKey.append(False)
    elif problem == 1:
        studentKey.append(True)

# Use a loop to ask for each correct answer
for numQs in range (1, numQs + 1):
    problemDx = int(input("What was the actual answer for question " + str(numQs) + "? Answer 1 for true or 0 for false. "))
    if problemDx == 0:
        teacherKey.append(False)
    elif problemDx == 1:
        teacherKey.append(True)




# Quiz percentage

for i in range(1, numQs + 1):
    
    if (studentKey[i - 1]) == (teacherKey[i - 1]):
        numRight += 1
    else:
        numRight += 0


grade = int((numRight / numQs) * 100)
print("\n")
print("=" * 40)
print(studentName + "'s Test Score")
print('=' * 40)
print(str(numRight) + "/" + str(numQs))
print(str(grade) + "%")
if grade < 70:
    passing = "Failed"
elif grade <= 70:
    passing = "Passed"
print("Passing: " + passing)
# Pass/Fail status