'''
Program: gradeReportProject.py
Author: Mason Curtis
Date: 11/4/25
'''


# Challenge: Complete Grade Book System

# Create a list of student dictionaries
'''Necessary:
name
id
math grade
ela grade
science grade
history grade
average
'''
student1 = {"name": "Emma Rodriguez",#input("student 1 - name: "),
            "id":"S12345",#input("student 1 - student id: "),
            "math_grade":95,#int(input("student 1 - math grade: ")),
            "english_grade":91,#int(input("student 1 - english grade: ")),
            "science_grade":92,#int(input("student 1 - science grade: ")),
            "history_grade":89,#int(input("student 1 - history grade: ")),
            }
student2 = {"name":"Marcus Chen",#input("student 2 - name: "),
            "id":"S12346",#input("student 2 - student id: "),
            "math_grade":87,#int(input("student 2 - math grade: ")),
            "english_grade":90,#int(input("student 2 - english grade: ")),
            "science_grade":85,#int(input("student 2 - science grade: ")),
            "history_grade":88#int(input("student 2 - history grade: ")),
            }
student3 = {"name":"Sophia Patel",#input("student 3 - name: "),
            "id":"S12347",#input("student 3 - student id: "),
            "math_grade":98,#int(input("student 3 - math grade: ")),
            "english_grade":96,#int(input("student 3 - english grade: ")),
            "science_grade":94,#int(input("student 3 - science grade: ")),
            "history_grade":97,#int(input("student 3 - history grade: ")),
            }

def average_grade(student):
    math = student["math_grade"]
    english = student["english_grade"]
    science = student["science_grade"]
    history = student["history_grade"]
    average_num = (math + science + history + history) / 4
    return average_num
average = average_grade(student1)
student1.update({"average": average})
average2 = average_grade(student2)
student2.update({"average": average2})
average3 = average_grade(student3)
student3.update({"average": average3})
grade_book = [
    # Add your student dictionaries here
    student1,
    student2,
    student3
]
def formatted_list(student):
    name = student["name"]
    id = student["id"]
    math = student["math_grade"]
    english = student["english_grade"]
    science = student["science_grade"]
    history = student["history_grade"]
    average_grade = student["average"]
    print("Student:",name)
    print("ID:",id)
    print("Math:",math)
    print("English:",english)
    print("Science:",science)
    print("History:",history)
    print("Average:",average_grade)
    print("-" * 30)
    print()

def print_class_report():
    """Prints a formatted report for all students"""
    print("=" * 50)
    print("CLASS GRADE REPORT")
    print("=" * 50)
    print("\n")
    print(formatted_list(student1))
    print(formatted_list(student2))
    print(formatted_list(student3))
    


def find_top_student(students):
    """Returns the student with the highest average"""
    avg1 = student1["average"]
    avg2 = student2["average"]
    avg3 = student3["average"]
    averages = [avg1,avg2,avg3]
    best_student = max(averages)
    if best_student == averages[0]:
        print("Top Student:",student1["name"])
        print("Average:",student1["average"])
    elif best_student == averages[1]:
        print("Top Student:",student2["name"])
        print("Average:",student2["average"])
    elif best_student == averages[2]:
        print("Top Student:",student3["name"])
        print("Average:",student3["average"])
    
    print()


def count_honor_students(students):
    """Counts students with average >= 90"""
    num_honors = 0
    # number of honors students (get averages, count with a variable to find how many)
    avg1 = student1["average"]
    avg2 = student2["average"]
    avg3 = student3["average"]
    if avg1 > 90:
        num_honors = num_honors + 1
    
    if avg2 > 90:
        num_honors = num_honors + 1
    if avg3 > 90:
        num_honors = num_honors + 1

    print("Honor Roll Students (avg >= 90):", num_honors)
    print("Total Students:",len(grade_book))


# Test your functions
print_class_report()

print("=" * 50)
print("CLASS STATISTICS")
print("=" * 50)
print()

top_student = find_top_student(grade_book)

honor_count = count_honor_students(grade_book)
