import math
def mul(n):
    mularr=[]
    j = 0
    while j<n:
        if j%3==0 or j%5==0:
            mularr.append(j)
        else:
            pass
        j += 1
    return numpy.sum(mularr)