from time import time
start = time()
def suma(n):
    a = 0
    for i in range(0, n+1):
        a = a + i
    return a
    
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
"""
a = 1
while len(factors(suma(a))) <500:
    a += 1
    print(a)

print(suma(a)) """
print(suma(7), time()-start)
