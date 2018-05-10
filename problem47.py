def prime_factors(n):
    x=2
    while n!=1:
        if not n%x:
            n//=x
            yield x
        else:
            x+=1
    
def counted_facs(m):
    factors = [x for x in prime_factors(m)] 
    fac_set = set()
    for i in factors:
        fac_set.add(i**factors.count(i))
    return sorted(fac_set)

def equal_lists(array1, array2):
    if len(array1)!=len(array2):
        return False
    for i in range(len(array1)):
        if array1[i]!=array2[i]:
            return False
    return True

    
upper=700
four_facs = [x for x in range(640,650) if len(counted_facs(x))==3]
print(four_facs)