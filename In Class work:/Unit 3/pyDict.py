'''

program: pyDict.py
Author: Mason Curtis
Date: 11/04/2025

- Student ID: "S12345"
- Grade Level: 12
- Email: "emma.r@school.edu"
- Math grade: 95
- English Grade: 88
- Science grade: 92
- Homework completed - true

Tasks:
1. Create a dictionary called student1 with all the information above
2. print the entire dictionary
3. Print just emma's email address
4. Print just Emma's math grade
'''

# Part 1: Create your dictionary here
student1 = {"name": "Emma Rodriguez",
            "student_id": "S12345",
            "grade_level": 12,
            "email": "emma.r@school.edu",
            "math_grade": 95,
            "english_grade": 88,
            "science_grade": 92,
            "homework_completed": True
            }

# Print the entire dictionary
print("Complete student record:")
print(student1)

# Print specific values
print("\nStudent email:", student1["email"])
print("Math grade:", student1["math_grade"])

# Part 2

# Modify her homework status
student1["homework_completed"] = False

# Update her english grade
student1["english_grade"] = 91

# Add a history grade
student1["history_grade"] = 89

# Add clubs information
student1["clubs"] = ["Debate Team", "Math Club"]

#Print the updated directory
print("\nUpdated student record:")
print(student1)


# Part 3: Create a function to calculate average grade
#Python function structure: def(keyword) func_name(argument)
def calculate_average(student):

    '''
    this function calculates the student average
    '''

    # Get all the grades
    math = student["math_grade"]
    science = student["science_grade"]
    history = student["history_grade"]
    english = student["english_grade"]
    

    # Calculate the average
    average_num = (math + history + english + science) / 4

    # Return the average
    return average_num
    
average = calculate_average(student1)
print(f"\n{student1['name']}'s average grade: {average:.2f}")


# Part 4: Using dictionary methods
'''
.keys(), .values(), .items(), .get(), .update()
'''

# Print all keys in the dictionary
student_keys = student1.keys()
print("\nAll values in the dictionary:", student_keys)
# Print all values
student_values = student1.values()
print("\nAll values in the dictionary:", student_values)
#print(student1.values)

# Print all key value pairs
student_items = student1.items()
print("\nAll the key-value pairs:", student_items)
for key, value in student1.items():
    print(f"{key}: {value}")
#print(student1.items())

#Safely get phone number (doesn't exist)
phoneNum = "###-###-####"
student1.update({"phone_number": phoneNum})
phone = student1.get("phone_number")
# student1.get("phone_number", "not available")

print("\n Phone number:", phone)


#
student2 = {
    "name": "Marcus Chen",
    "student_id": "S123456"
}


# Update grade to 11, math to 87, ela to 90, and science to 85

student2.update({
    "grade_level": 11,
    "math_grade": 87,
    "english_grade": 90,
    "science_grade": 85
})
#

print("\nNew student information:", student2)
#


