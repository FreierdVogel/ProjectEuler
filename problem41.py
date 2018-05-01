from itertools import count
def sixn():
    yield 2
    yield 3
    for i in count(1):
        i=6*i+1
        yield i 
        yield i-2
def sieve(m):
    sieve_ = [True]*m
    for i in sixn():
        if i>m:
            break  
        else:
            if sieve_[i]:
                yield i 
                for mult in range(i*i, m, i):
                    sieve_[mult]=False

for x in sieve(5455):
    pass   