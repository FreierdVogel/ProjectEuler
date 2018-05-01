def is_bin_pal(n):
    return bin(n)[2:]==bin(n)[2:][::-1] and n==int(str(n)[::-1])

print(sum(x for x in range(10**6) if is_bin_pal(x)))