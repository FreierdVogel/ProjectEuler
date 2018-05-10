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
limit = 10 ** 6
primes = list(prime_until(limit))
primeSet = set(primes)
length = len(primes)
result = []

for i in range(0, length):
    for j in range(i + 2, length):
        v = sum(primes[i:j])
        if v > limit:
            break
        if v in primeSet:
            result.append((j - i, v))
print(max(result))