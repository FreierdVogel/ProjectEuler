from math import sqrt
from time import time
def fac(n):    
    yield from(k for i in range(1, int(sqrt(n)) + 1) if n % i == 0 for k in (i, n // i))
	
def amic(m):
	n = sum(fac(m))-m
	if n==sum(fac(n))-m:
		return  True
	return False
print(amic(6))
t0 = time()
a = 0
for i in range(10001):
	if amic(i):
		if sum(fac(i))-i == i:
			pass
		else:
			print(i, sum(fac(i))-i)
			a+=sum(fac(i))
print(a//2, time()-t0)