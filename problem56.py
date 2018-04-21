i = 0
j = 0
for a in range(1, 100):
	for b in range(1, 100):
		i = sum([int(x) for x in str(a**b)])
		if i>j:
			j = i

print(j)