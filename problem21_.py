from functools import reduce
from math import sqrt
from time import time
def fac(n):    
    a = 0
    for i in range(1, sqrt(n+1):
        if n%i==0:
            a+=i
    return a
	
def amic(m):
	n = fac(m)
	if n==fac(n):
		return  True
	return False
print(amic(6))
t0 = time()
a = 0
for i in range(10001):
	if amic(i):
		if fac(i) == i:
			pass
		else:
			print(i, fac(i))
			a+=fac(i)
print(a//2, time()-t0)