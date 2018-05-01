def fac(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
    return a

print(fac(5)) 

def c(a,b):
    if b>a:
        return False
    return fac(a)//(fac(b)*fac(a-b))
cont = 0
for i in range(2, 101):
    for j in range(2, 101):
        if c(i, j)>10**6:
            cont += i
print(cont)