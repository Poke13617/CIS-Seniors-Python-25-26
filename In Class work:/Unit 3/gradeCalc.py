exam1_grade = float(input("Enter score on Exam 1 (out of 100): "))
exam2_grade = float(input("Enter score on Exam 2 (out of 100): "))
exam3_grade = float(input("Enter score on Exam 3 (out of 100): "))

total_exam_points = exam1_grade + exam2_grade + exam3_grade
avg_exam_points = total_exam_points/3
print(f"\nYour overall grade is: {avg_exam_points:.2f}")


def calculate_grade(points):
    total_points = int(input("Please enter the number of points for this assignment: "))
    grade = points / total_points
    return grade

assign1_grade = float(input("Enter number of points on Assignment 1 (out of 50): "))
assign2_grade = float(input("Enter number of points on Assignment 2 (out of 50): "))
assign3_grade = float(input("Enter number of points on Assignment 3 (out of 50): "))
assign4_grade = float(input("Enter number of points on Assignment 4 (out of 50): "))

assign1_grade = calculate_grade(assign1_grade)
assign2_grade = calculate_grade(assign2_grade)
assign3_grade = calculate_grade(assign3_grade)
assign4_grade = calculate_grade(assign4_grade)

assign1 = float(input("Enter number of points on Assignment 1 (out of 50): "))
assign2 = float(input("Enter number of points on Assignment 2 (out of 50): "))
assign3 = float(input("Enter number of points on Assignment 3 (out of 75): "))
assign4 = float(input("Enter number of points on Assignment 4 (out of 75): "))

grade1 = calculate_grade(assign1)
grade2 = calculate_grade(assign2) 
grade3 = calculate_grade(assign3)
grade4 = calculate_grade(assign4)

total_assignment_points = assign1_grade + assign2_grade + assign3_grade + assign4_grade 
avg_assignment_points = (total_assignment_points / 4) * 100

total_assignment_points_2 = (grade1 + grade2 + grade3 + grade4)
average_assignment_points_2 = (total_assignment_points / 4) * 100
overall_grade = (0.5 * avg_exam_points) + (0.4 * avg_assignment_points) + (0.1 * average_assignment_points_2)

print(f"\nStudent overall average on programming assignments set 1: {avg_assignment_points:.2f}")

print(f"Student overall average on programming assignments set 2: {average_assignment_points_2:.2f}")

print(f"\nYour overall grade is: {overall_grade:.2f}")