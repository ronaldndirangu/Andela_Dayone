def is_prime(n):
    prime_numbers = [2, 3]
    for num in range(4, n):
        status = False
        for prime in prime_numbers:
            if num % prime == 0:
                status = True
        if status == False:
            prime_numbers.append(num)

    for n in prime_numbers:
        print (n)
