# Python Variable Name Validator
# Student Name: Mason Curtis
# Date: 0/7/25

# List of Python keywords
python_keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield'
]
invalid_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(',
      ')', '-', '+', '=', '{', '}', '[', ']', '|',
        '\ ', ';', ':', ' ', ',', '.', '<', '>',
          '/', '?', '\n', '\t'
]
# Display welcome message
print("=== PYTHON VARIABLE NAME VALIDATOR ===")
print("This program checks if your variable name is valid in Python.")
print()

# Get user input
variable_name = input("Enter a variable name to validate: ")

variable_num_count = len(variable_name)
# Your validation code goes here
for i in range(1, 35):
    if variable_name == python_keywords[i]:
        invalid_name = True
        invalid_used = python_keywords[i]
        break
    else:
        invalid_name = False
        checkIdentifier = variable_name.isidentifier()
        if checkIdentifier == True:
            invalid_name = False
        else:
            invalid_name = True
            invalid_used = python_keywords[i]
# Check each rule and provide appropriate feedback
if invalid_name == True:
    print("The name is invalid, the name " + str(invalid_used) + " was invalid as it's a python selector.")
else:
    print("Name validated")