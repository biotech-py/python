name =  int(input("Enter Total Students:"))
Datastudent = []
for i in range(name):
    print(f"Enter Details of the Students{i+1}")
    name = input(" Name:")
    roll_no = int(input("Roll Number:"))
    marks = int(input("Marks:"))
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
        "NAME": name,
        "ROLL_NO": roll_no,
        "Marks": marks,
        "Grades": grades