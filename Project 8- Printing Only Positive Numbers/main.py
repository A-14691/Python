# Read numbers from user input
user_input = input("Enter numbers separated by spaces: ")

numbers = [int(num) for num in user_input.split()]

print("Positive numbers:")
i = 0

while i < len(numbers):
    if numbers[i] > 0:
        print(numbers[i])
    i += 1
