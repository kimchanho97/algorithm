# 4
# 1 3
# 2 5
# 3 5
# 6 7

import sys
n = int(sys.stdin.readline())
lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
lines.sort()

curL, curR = lines[0][0], lines[0][1]
result = 0
for line in lines:
    left, right = line
    if left <= curR:
        curR = max(curR, right)
    else:
        result += (curR - curL)
        curL, curR = left, right
result += (curR - curL)
print(result)