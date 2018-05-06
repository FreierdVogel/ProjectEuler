def  sum_of_div_until(m):
    yield 0
    yield 1
    sieve = [1]*m
    for i in range(2, m):
        yield sieve[i]
        for mul in range(i,m,i):
            sieve[mul]+=i
    
upper = 28123
sum_until = [j for j in sum_of_div_until(upper)]
abundants = set(j for j in range(12, upper) if sum_until[j]>j)

def can_be_written(n):
    for i in abundants:
        if i>n:
            break
        elif n-i in abundants:
            return False
    return True

print(sum([x for x in range(upper) if  can_be_written(x)]))