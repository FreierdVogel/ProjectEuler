from os.path import join
from string import ascii_uppercase as ABC

with open(join("..", "projecteuler", "p022_names.txt")) as f:
    names = sorted(f.read().replace('"', "").split(","))


def value(word):
    return sum(ABC.index(i) for i in word) + len(word)

print(sum((a + 1) * value(i) for a, i in enumerate(names)))