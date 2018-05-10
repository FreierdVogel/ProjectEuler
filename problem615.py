def len_fac(n):
    x = 2
    lenz = 0
    while n>1:
        if not n%x:
            n=n//x
            lenz += 1
        else:
            x+=1
        
for i in range(51234)