n=40000
a=(n+n+n)*(n+1)//2
b=n*(n+n+n-1)//2 
c=n*(n+n-1)
while not a==b==c:
    print(n)
    a=(n+n+n)*(n+1)//2
    b=n*(n+n+n-1)//2 
    c=n*(n+n-1)
    n+=1
print(n)