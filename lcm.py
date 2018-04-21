def lcm(a, b):
    fac_a=[]
    fac_b=[]
    for i in range(a*b):
        fac_a.append(i*a)      
        fac_b.append(i*b)
    return min([x for x in fac_a if x in fac_b])

print(lcm(123,12213))
