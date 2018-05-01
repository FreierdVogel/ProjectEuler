def fact(n):
    a = 1
    for i in range(1, n+1):
        a*=i
    return a
def is_digit(n):
    return sum(fact(int(x)) for x in str(n))==n

print(is_digit(145))
print(sum(x for x in range(100000)  if is_digit(x) and x!=1 and x!=2))