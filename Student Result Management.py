students = {
    "Ram": 75,
    "Sita": 85,
    "Hari": 62,
    "Gita": 90,
    "Rita": 48
}

for name, marks in students.items():
    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("Name:", name, "| Marks:", marks, "| Result:", result)

top_student = max(students, key=students.get)

print("Student with highest marks:", top_student)
print("Highest marks:", students[top_student])