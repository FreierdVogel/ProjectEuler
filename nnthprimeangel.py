from itertools import count
from timeit import default_timer as timer
start = timer()
def sixn():
    yield 2
    yield 3
    for i in count(1):
        x = 6 * i + 1
        yield x - 2
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

print(sum(primes_until(135)), timer() - start)