# 5 4
# 1
# 4
# 7
# 10
# 13

import sys

n, m = map(int, sys.stdin.readline().split())
lst = sorted(int(sys.stdin.readline()) for _ in range(n))

minL = 1
maxL = (lst[n-1] - lst[0]) // (m-1)
result = 1
while minL <= maxL:
    curL = (minL + maxL) // 2
    prevP = lst[0]
    cnt = 1
    for i in range(1, n):
        curP = lst[i]
        dist = curP - prevP
        if dist >= curL:
            cnt += 1
            prevP = curP

    if cnt >= m:
        result = max(result, curL)
        minL = curL + 1
    else:
        maxL = curL - 1

print(result)