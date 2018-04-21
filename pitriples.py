from time import time
start = time()
for n in range(1, 1000):
	for m in range(1, 1000):
		if m>n:
			pass
		else:
			a = n**2 - m**2
			b = 2*n*m
			c = n**2 + m**2
			if a + b + c == 1000:
				print(a, "*", b, "*", c, "=", a*b*c)
print(time() - start)
				