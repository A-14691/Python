number = int(input("Enter a number: "))

while number < 0:
    number = int(input("Enter a non-negative number: "))

factorial = 1
value = 1
while value <= number:
    factorial *= value
    value += 1

print(f"The factorial of {number} is {factorial}.")