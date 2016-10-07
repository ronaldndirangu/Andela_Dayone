def fib(num):
    a=0
    b=1
    for i in range(0,num-1):
        print(a)

        temp=a
        a=b
        b=temp+b
    return a


    

