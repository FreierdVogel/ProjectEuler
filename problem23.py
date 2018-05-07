from time import time
def  divs_sum_til(m):
    yield 0
    yield 1
    sieve=[1]*m
    for i in range(2,m):
        yield sieve[i]
        for k in range(i, m, i):
            sieve[k]+=i

def not_can_be_written(m):
    for i in abundants:
        if i>m:
            break
        if m-i in abundants:
            return False
    return True
t0 = time()
upper=28123
sums=[x for x in divs_sum_til(upper)]
abundants=set(x for x in range(12,upper) if sums[x]>x)

print(sum(tuple(x for x in range(upper) if not_can_be_written(x))), time()-t0)