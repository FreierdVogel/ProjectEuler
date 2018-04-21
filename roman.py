def arab(n):
    R = {"O": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    a = 0
    for i in range(0, len(n)-1):
        if n[i]>n[i+1]: 
           a += R[n[i]] + R[n[i+1]]
        """elif n[i]<n[i+1]:
            pass
        if n[i]>n[i-1]:
            a += R[n[i]] - R[n[i-1]]"""
        
    return a + R[n[-1]]

print(arab("VI"))
