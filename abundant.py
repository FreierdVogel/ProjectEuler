def fac(n):
    yield from(k for i in range(1, int(pow(n, .5)) + 1) if n % i == 0 for k in (i, n // i))
def abundant(n):
    if (sum(fac(n))-n)==n:
        return True
    return False

print(abundant(28))