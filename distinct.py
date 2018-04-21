def dist(a, b):
    pow = set({})
    for i in range(2, a+1):
        for j in range(2, b+1):
            pow.add(i**j)
    return  len(pow)

print(dist(100,100))


    