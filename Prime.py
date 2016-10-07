def is_prime(number):
    for num in range(number):
        for p in range(2,num):
            if (num%p==0):
                break
            else:
                print (num)
                break

