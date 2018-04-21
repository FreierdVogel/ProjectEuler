from timeit import default_timer as timer
def es_primo(n):
	for i in range(3, n, 2):
		if n%i==0:
			return False
	if n%2==0:
		return False
	return True
s = 50000

start = timer()
v = [x for x in range(2, s) if es_primo(x)!=False]
a = [j for j in range(1, s, 2) if j not in v]
print(a,"\n", "t1 = ", timer() - start, "\n", sum(a))
