def fi(n):
    cont = 0
    for i in range(2,n,2):
        if n%i!=0:
            cont+=1
    return cont

def es_primo(n):
    for i in range(3,n,2):
        if n%i==0:
            return False
    return True

print(es_primo(20))