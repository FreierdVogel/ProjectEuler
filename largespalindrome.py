import stopwatch
def pal(n):#Hasta n
    pals = []
    for i in range(n):
        for j in range(n):
            if str(j*i)==str(j*i)[::-1] and i!=0:
                pals.append(j*i)
    return max(pals)
print(stopwatch.crono(pal(10000)))
