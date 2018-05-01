from time import time
start = time()
for a in range(500):
	for b in range(500):
		c = 1000 - a - b
		if a**2 + b**2==c**2:
			print(a*b*c)
			break
print(time() - start)
				