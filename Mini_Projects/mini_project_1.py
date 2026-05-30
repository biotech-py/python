total_students = int(input("Enter Total Students: "))

Datastudent = []

for i in range(total_students):
    print(f"\nEnter Details of Student {i+1}")

    name = input("Name: ")
    roll_no = int(input("Roll Number: "))
    marks = int(input("Marks: "))

    if marks > 90:
        grades = "EX"
    elif marks > 80:
        grades = "A"
    elif marks > 70:
        grades = "B"
    elif marks > 60:
        grades = "C"
    elif marks >= 35:
        grades = "D"
    else:
        grades = "F"

    students = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grades": grades
    }

    Datastudent.append(students)

print("\nAll Students Data")

for s in Datastudent:
    print(f"{s['name']} - Roll Number: {s['roll_no']} - Marks: {s['marks']} - Grades: {s['grades']}")