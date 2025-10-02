'''
Filename: pyQuiz1.py
Author: Mason Curtis
Description: Python Quiz 1
'''

# Question 1
for i in range(0,6):
    number = i
    print(str(i))
print("\n\n")
# Question 2
for i in range (3,9):
    print(str(i))

print("\n\n")

# Question 3
for i in range (0,11,2):
    print(i)
print("\n\n")

# Question 4
for i in range (10, 0, -1):
    print(i)
print("\n\n")

# Question 5
for i in range(1, 6):
    print("5 X " + str(i) + " = " + str(i * 5))
print("\n\n")
# Question 6
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
elif age > 18:
    print("You are an adult")
print("\n\n")

# Question 7
for i in range(1, 11):
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")
print("\n\n")

# Question 8
for i in range (20, -1, -5):
    print("Countdown: " + str(i))
print("\n\n")

# Question 9
for i in range(1, 7):
    if i < 4:
        print("Number " + str(i) + " is Small.")
    else:
        print("Number " + str(i) + " is Large")
print("\n\n")

# Question 10
number = int(input("Enter a number: "))
for i in range(1, number, 2):
    if i < 5:
        print("Low: " + str(i))
    elif i >= 5:
        print("High: " + str(i))