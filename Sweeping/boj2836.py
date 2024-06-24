# 8 15
# 1 12
# 3 1
# 3 9
# 4 2
# 7 13
# 12 11
# 14 11
# 14 13

import sys

n, m = map(int, sys.stdin.readline().split())
lines = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a <= b:
        continue
    lines.append((b, a))
lines.sort()

if lines:
    curL, curR = lines[0][0], lines[0][1]
    total = 0
    for line in lines:
        l, r = line
        if l <= curR:
            curR = max(r, curR)
        else:
            total += (curR - curL)
            curR, curL = r, l
    total += (curR - curL)
    print(m + 2*total)

else:
    print(m)