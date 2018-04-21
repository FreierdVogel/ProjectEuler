def fibindex(n):
    a, b = 1, 1
    cont = 1
    while len(str(a))<n:
        a, b = b, b+a
        cont += 1
    return cont

print(fibindex(2))