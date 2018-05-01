def is_palin(n):
    return n==int(str(n)[::-1])
j = 0
for x in range(1,10001):
    a = 0
    while a<51:
        if is_palin(x + int(str(x)[::-1])):
            break
        else:
            x += int(str(x)[::-1])
            a+=1
        if a==50:
            j+=1
            break
print(j)
  