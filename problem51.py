def prime_factors(n[,m]):
    x=2
    while n!=1:
        if not n%x:
            n//=x 
            yield x
        else:
            x+=1

