from time import time
from itertools import count
def sixn():
    yield 2
    yield 3
    for i in count(1):
        i=6*i+1
        yield i
        yield i-2

def prime_until(m):
    sieve = [True]*m
    for i in sixn():
        if i>m:
            break
        if sieve[i]:
            yield i
            for mult in range(i*i, m, i):
                sieve[mult]=False


upper = 10**6
t0 = time()
set_primes = set(x for x in prime_until(upper))
list_primes = sorted(list(set_primes))
mx=0
mx_len=0
actual=0
for i in range(len(set_primes)//2):
    #print(i)
    for j in range(i, len(set_primes)):
        if j<i:
            continue
        if sum(list_primes[i:j]) in set_primes:
            actual=len(list_primes[i:j])
            if actual>mx_len:
                mx_len=actual
                mx=sum(list_primes[i:j])
        
print(mx, time()-t0)

