from functools import lru_cache
from collections import defaultdict

polymer = ""
rules = dict()
with open("input.txt", "r") as file:
    lines = file.readlines()
    polymer = lines[0].strip()
    for line in lines[2:]:
        a, b = line.strip().split("->")
        rules[a.strip()] = b.strip()

@lru_cache(maxsize=None)
def step2(a, b, n):
    if n == 0:
        return dict()
    c = rules[a+b]
    sub_l = step2(a, c, n-1)
    sub_r = step2(c, b, n-1)
    counts = defaultdict(int)
    for k, v in sub_l.items():
        counts[k] += v
    for k, v in sub_r.items():
        counts[k] += v
    counts[c] += 1
    return counts

n = 40
new_ply = ""
c = defaultdict(int)
for i in range(1, len(polymer)):
    sub = step2(polymer[i-1], polymer[i], n)
    for k, v in sub.items():
        c[k] += v
c[polymer[-1]] += 1
values = c.values()
print(max(values) - min(values))
