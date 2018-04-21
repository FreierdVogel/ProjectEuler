def sumsqdif(n):
    a = 0
    b = 0
    for i in range(n+1):
        a = a + i**2
        b = b + i
    return b**2-a
print(sumsqdif(100))