def is_pal(n):
    return n==int(str(n)[::-1])
n = 349
a = 1
while a<50:
    if is_pal(n + int(str(n)[::-1])):
        print(n + int(str(n)[::-1]))
        break
    else:
        n += int(str(n)[::-1])
        print(n)
        a+=1
print(a)