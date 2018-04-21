def primo_numero(max):
    contador = 1
    n = 1
    no_primos = set()
    while contador < max + 1:
        n += 1
        if n not in no_primos:
            contador += 1
            no_primos.update(range(n * 2, max * 15, n))
    return n
print(primo_numero(10001))
