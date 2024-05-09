# 5
# 1 2 3 4 5
# 4
# 1 3 4 6
# 2 3
# 1 1 3 -2
# 2 3

import sys

def update(i, diff):
    while i <= n:
        tree[i] += diff
        i += (i & -i)
    return

def prefix_sum(i):
    total = 0
    while i >= 1:
        total += tree[i]
        i -= (i & -i)
    return total

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
tree = [0] * (n + 2)  # 1 ~ n+1
m = int(sys.stdin.readline())
for _ in range(m):
    command = sys.stdin.readline().strip()
    if command[0] == "1":
        a, b, c, d = map(int, command.split())
        update(b, d)
        update(c+1, -d)
    else:
        a, b = map(int, command.split())
        diff = prefix_sum(b)
        # print(diff)
        print(diff + lst[b-1])