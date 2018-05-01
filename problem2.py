def fib(n):
    a, b =  1, 2
    i = 0
    while  a<n:
        if a&1==False:
            i+=a
        a, b  = b, b+a
    return i

print(fib(4*10**6))