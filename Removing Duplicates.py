numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)