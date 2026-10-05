for num in range(1, 51):
    if num < 2:
        continue
    if num > 2 and num % 2 == 0:
        continue

    is_prime = True
    for divisor in range(3, int(num ** 0.5) + 1, 2):
        if num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
