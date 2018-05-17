from time import time
from itertools import count
def sixn():
    yield 2
    yield 3
    for i in count(1):
        i=6*i+1
        yield i-2
        yield i

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
list_primes = list(prime_until(upper))
set_primes = set(list_primes)
mx=0
mx_len=0
actual=0
top=len(list_primes)
result = []
for i in range(top):
    for j in range(i+2, top):
        v=sum(list_primes[i:j])
        if v>upper:
            break
        if v in set_primes:
            actual=j-i
            result.append((actual, v))
print(max(result)[1], time()-t0)
