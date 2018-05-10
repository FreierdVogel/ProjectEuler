from itertools import count 
def pentagonals_until(m):
    for n in count(1):
        yield n*(n+n+n-1)//2
print(list(pentagonals_until(10)))
