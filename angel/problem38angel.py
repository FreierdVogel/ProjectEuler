import time
t0 = time.time()

#932718654

def condecadenated(n, r):
    result = ""
    for i in range(1, r + 1):
        result += str(n * i)
    return result

def is_pandigital(s):
    return sorted(s) == sorted("123456789")
        
result = ""
for i in range(10000):
    if is_pandigital(condecadenated(i, 6 - len(str(i)))):
        if condecadenated(i, 6 - len(str(i))) > result: result = condecadenated(i, 6 - len(str(i)))
print(result)

print("It took {} ms".format(int((time.time() - t0) * 1000)))