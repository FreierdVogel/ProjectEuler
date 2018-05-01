from math import sqrt
from time import time
t0 = time()
max_=0
p_=0
for p in range(1, 1000):
    usados = set()
    print(p)
    cont=0
    for a in range(1,p//2):
            for b in range(1,p-2*a):
                c = sqrt(a**2+b**2)
                if a + b + c==p:
                    cont+=1
    if cont>max_:
        print("Actualización, ahora el mayor número es", p, "con", cont, "iteraciones")
        max_=cont
        p_=p
    if cont==max_:
        print("Hm,", p,  "es igual al anterior")

print(p_//2, time()-t0)