from math import sqrt
from time import time
def fac(n):    
    a = 0
    for i in range(1,n//2+1):
        if n%i==0:
            a+=i
    return a
def is_abund(n):
    if fac(n)>n:
        return True 
    return False

a = 0
for i in range(1, 28124):
    if 
