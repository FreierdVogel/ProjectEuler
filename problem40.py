
a=[]
for i in range(10**6+1):
    a.append(str(i))
a="".join(a)

print(int(a[1])*int(a[10])*int(a[100])*int(a[1000])*int(a[10000])*int(a[100000])*int(a[1000000]))  