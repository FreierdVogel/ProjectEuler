from time import time
from itertools import count
from math import sqrt, pow
def sixn():
    yield 2
    yield 3
    for i in count(1):
        i=6*i+1
        yield i-2
        yield i
def primes_until(m):
    sieve=[True]*m
    for i in sixn():
        if i>m:
            break
        if sieve[i]:
            yield i
            for mult in range(i*i, m, i):
                sieve[mult]=False
"""def can_be_written(n):
    sqrtn=int(sqrt(n))
    foursSqrtn=int(sqrt(sqrtn))
    #eigthSqrtn=int(sqrt(foursSqrtn))
    for i in primes_list:
        if i>foursSqrtn:
            break
        for j in primes_list:
            if j>sqrtn:
                break
            if (n-i**4-j**2)**(1/3) in primes_set:
                #print(i,"^4 + ", j, "^2 + ", int((n-i**4-j**2)**(1/3)), "^3 = ",  n, sep="")
                return True
    return False"""
primes_list=list(primes_until(100000))
primes_set=set(primes_list)
top=5*10**7
count=0
t0=time()
numbers=set()
for p2 in primes_list:
    p2=p2**2
    if p2>top:
        break
    for p3 in primes_list:
        p3=p3**3
        if p3>top-p2:
            break
        for p4 in primes_list:
            #print(p2,"**4 + ", p3, "**3 + ", p4, "**2 = ", p2**4+p3**3+p4**2, sep="")
            k=p2+p3+p4**4
            if k<top:
                numbers.add(k)
            elif k>top:
                break
                #print(p2,"**2 + ", p3, "**3 + ", p4, "**4 = ", p2**2+p3**3+p4**4, sep="")
print(len(numbers), time()-t0)