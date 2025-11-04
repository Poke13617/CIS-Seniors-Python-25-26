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
grade_book = [
    # Add your student dictionaries here
    student1,
    student2,
    student3
]

def print_class_report(students):
    """Prints a formatted report for all students"""
    # Your code here
    #pass

'''
def find_top_student(students):
    """Returns the student with the highest average"""
    # Your code here
    #pass

def count_honor_students(students):
    """Counts students with average >= 90"""
    # Your code here
    #pass
'''
# Test your functions
print_class_report(grade_book)

#top_student = find_top_student(grade_book)
#honor_count = count_honor_students(grade_book)