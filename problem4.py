from time import time
def pal(n):
    return n==int(str(n)[::-1])
t0 = time()
print(max(i*j for i in range(100,1000) for j in range(100,1000) if pal(i*j)), time()-t0)