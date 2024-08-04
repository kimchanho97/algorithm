# 7
# -2 -3 -24 -6 98 100 61

import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
result = abs(lst[0] + lst[1] + lst[n-1])
answer = [0, 1, n-1]

for i in range(n):
    l, r = i+1, n-1
    center = lst[i]
    while l < r:
        # 두개의 합이 -center가 되어야 함
        curSum = lst[l] + lst[r]
        if abs(curSum + center) < result:
            result = abs(curSum + center)
            answer = [i, l, r]

        if curSum < -center:
            l += 1
        elif curSum == -center:
            break
        else:
            r -= 1

# print(answer)
for i in answer:
    print(lst[i], end=" ")