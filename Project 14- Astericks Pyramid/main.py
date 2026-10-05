# Print a pyramid pattern of asterisks with 5 levels
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()
