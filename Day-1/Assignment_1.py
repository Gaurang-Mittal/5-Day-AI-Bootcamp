import random

# Generate a list of 10 random numbers
numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))

# Print the complete list
print("All numbers:", numbers)

# Print even numbers
print("Even numbers:")

for num in numbers:
    if num % 2 == 0:
        print(num)