def fact(n):
    if fact(n-1)>1:
        return n*fact(n-1)
    else: 
        pass
print(fact(5))