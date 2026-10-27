marks = {
    "Python": int(input("Enter Python marks: ")),
    "Database": int(input("Enter Database marks: ")),
    "Mathematics": int(input("Enter Mathematics marks: "))
}

total = sum(marks.values())
average = total / len(marks)

if average >= 40:
    result = "Pass"
else:
    result = "Fail"

print("Marks:", marks)
print("Total marks:", total)
print("Average marks:", average)
print("Result:", result)