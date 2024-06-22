# 6 4 3 5 1 2 8 9 7 10

import sys

def update(i, num):
    while i <= n:
        fenwick_tree[i] += num
        i += (i & -i)

def prefix_sum(i):
    total = 0
    while i >= 1:
        total += fenwick_tree[i]
        i -= (i & -i)
    return total


arr = list(map(int, sys.stdin.readline().split()))
n = len(arr)
fenwick_tree = [0] * (n + 1)
r = [0] * n
for i, val in enumerate(arr):
    temp = 0
    if val > 1:
        temp = prefix_sum(val - 1)
    r[i] = temp
    update(val, 1)
print(*r)