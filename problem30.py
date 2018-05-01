"""FUERZA BRUTA"""
from time import time
def is_(n):
    if sum(int(x)**5 for x in str(n))==n  and n!=1:
        return True
    return False
i =  0
t0 =  time()


print(sum(x for x in  range(10**6) if   is_(x)), time()-t0)
