from math import sqrt
from functools import reduce
from operator import mul
def fac(n):
    yield from(k for k in range(1, int(sqrt(n))+1) for j in range(1, n//2+1) if n%j==0)
a = 1
print(reduce(mul, []))

