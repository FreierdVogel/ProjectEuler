from math import sqrt

def is_abundant(n):
	return sum([k for i in range(1, int(sqrt(n))+1) if n % i == 0 for k in (i, n // i) if k!=n])>n

print(is_abundant(12))
v = 28123 
j = set()
abun = [x for x in range(12, v+1) if is_abundant(x)]
for i in range(12,v+1):
    print(i)
    for n in abun:
        if n>i or is_abundant(i-n):
            break
        if not is_abundant(i-n):
            j.add(n)
            #print(i, n)
print(sum(j))