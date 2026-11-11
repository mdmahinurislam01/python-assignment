# Problem 1: Student Grade Calculator

# 1. Input student name
student_name = input("Enter student name: ")

# 2. Input marks for 3 subjects
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# 3. Calculate total and average
total_marks = mark1 + mark2 + mark3
average_marks = total_marks / 3

# 4. Determine grade
if 80 <= average_marks <= 100:
    grade = "A+"
elif 70 <= average_marks < 80:
    grade = "A"
elif 60 <= average_marks < 70:
    grade = "B"
elif 50 <= average_marks < 60:
    grade = "C"
else:
    grade = "F"

# 5. Display result using f-string
print("\n--- Result ---")
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks:.0f}" if total_marks.is_integer() else f"Total Marks: {total_marks}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")
