
from itertools import combinations

s, k = input().split()
k = int(k)
s = sorted(s)

for i in range(1, k + 1):
    print(*map(''.join, combinations(s, i)), sep = '\n')