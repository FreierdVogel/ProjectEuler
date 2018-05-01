from math import sqrt
from time import time
from itertools import count

def abundants(n):
	while n>1:
		a=0
		for i in range(1,  n//2+1):
			if n%i==0:
				a+=i
		if a>n:
			yield n
		n -= 1

t0 = time()
v = 28124
a = [x for x in abundants(v)]
print("Done,  he tardado", time() - t0)
cont = 0
for i in range(12,v):
    for j in a:
        if i-j not in a:
            cont += i
print(time()-t0, len(a), cont)