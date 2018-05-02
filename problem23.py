from math import sqrt
#def fac(n):
    #sum(k for i in range(1, int(sqrt(n))+1) if n % i == 0 for k in (i, n // i) if k!=n)
def is_abundant(n):
	return sum([k for i in range(1, int(sqrt(n))+1) if n % i == 0 for k in (i, n // i) if k!=n])>n

print(is_abundant(12))
v = 30
j = 0
for i in range(12,v//2):
    
    if is_abundant(i):
        continue
    print(i)
    for n in range(i):
        #print(n)
        if not is_abundant(n):
            print(n, i)
            j += n
print(j)