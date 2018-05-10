"""
1.- Lista de primos
2.- Comprobar en un for in range(n), siendo n impar si se compone de un primo y un doble square
    -Usar eval()?
3.- Generalizar con while.(Cuando sea falso printear n)
"""
from itertools import count
from math import sqrt
def sixn():
    yield 2
    yield 3
    for i in count(1):
        x = 6*i+1
        yield x-2
        yield x


def primes_until(m):
    sieve = [True] * m
    for i in sixn():
        if i > m:
            break
        if sieve[i]:
            yield i
            for mult in range(i * i, m, i):
                sieve[mult] = False
def is_goldbach(n):
    for i in primes_list:
        if i>n:
            break
        for x in range(0, i):
            if i+2*x*x==n:
                #print(i, "+ 2 *", str(x)+"^2")
                return True
    return False

top=100000
primes_list=list(primes_until(top))
iterator=5

print(is_goldbach(17))
while is_goldbach(iterator):
    #print(iterator)
    if primes_list[-1]<iterator:
        print(top)
        top+=100000
        primes_list=list(primes_until(top))
    iterator+=2
print(iterator)
