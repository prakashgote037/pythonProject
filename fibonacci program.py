def fib(n):
    a = 0
    b = 1
    if n <= 0:
        print("Out of bound")


    else:
        print(a)
        print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        if c <= 89:
            print(c)

        else:
            print("Out of bound")
            break


fib(13)
