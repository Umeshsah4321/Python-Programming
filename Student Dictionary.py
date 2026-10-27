student = {
    "name": "Umesh",
    "age": 20,
    "class": "BSc Computer Science",
    "grade": "A"
}

print("Student Information")

for key, value in student.items():
    print(key.capitalize(), ":", value)