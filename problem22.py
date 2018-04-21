from os.path import join
from string import ascii_uppercase as ABC

with open(join("..", "projecteuler", "p022_names.txt")) as f:
    names = sorted(f.read().replace('"', "").split(","))
i =  0
for  j in range(0, len(names)):
    a = 0
    for x in names[j]:
        a += ABC.index(x)+1
    i += a*(j+1)
print(i)