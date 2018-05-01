from time import time

def pri_fac(n):
    x=2
    n = n//2
    while n>1:
        if n%x==0:
            n = n//x
            yield x
        else:
            x+=1
def pri_fac_(n):
    n//=2
    x=2
    a=0
    while n>1:
        if n%x==0:
            n = n//x
            a = x
        else:
            x+=1
    return a
t0 = time()
v = 5787231568
n = [x for x in pri_fac(v)]
end = time()
m = pri_fac_(v)
print(n, m, time()-end, end-t0)