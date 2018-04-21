from  time import time
def coll(n):
    cont = 0
    while n > 1:
        if n&1:
            n = n + n + n + 1
        else:
            n = n//2
        cont+=1
    return cont + 1

print(coll(13))
t0 = time()
"""i = 1
j = 1
for x in range(0,10**6):
    j = x
    if coll(j) > coll(i):
        i = x"""


print(max(range(2, 10 ** 6), key=coll), time()-t0)
