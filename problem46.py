"""
1.- Lista de primos
2.- Comprobar en un for in range(n), siendo n impar si se compone de un primo y un doble square
3.- Generalizar con while.(Cuando sea falso printear n)
"""
from itertools import count
from time import time
from math import sqrt
def sixn():
    yield 2
    yield 3
    for i in count(1):
        x = 6*i+1
        yield x-2
        yield x
def primes_until(m):
    sieve = [True]*m
    for i in sixn():
        if i>m:
            break
        if sieve[i]:
            yield i
            for mult in range(i*i, m, i):
                sieve[mult] = False
def is_goldbach(n):
    for x in range(n):
        if n-2*x**2 in primes_set:
                return True
    return False
t0=time()
top=100000
primes_list=list(primes_until(top))
primes_set=set(primes_list)
iterator=3
while is_goldbach(iterator):
    if primes_list[-1]<iterator:
        print(top)
        top+=100000
        primes_list=list(primes_until(top))    
    iterator+=2
print(iterator, time()-t0)

