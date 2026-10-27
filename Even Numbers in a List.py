numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Even numbers:")

for num in numbers:
    if num % 2 == 0:
        print(num)