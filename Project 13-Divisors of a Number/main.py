# Program to print all divisors of a number using a for loop

num = int(input("Enter an integer: "))
print(f"Divisors of {num} are:")

for i in range(1, num + 1):
    if num % i != 0:
        continue
    print(i)