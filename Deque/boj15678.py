# 10 2
# 2 7 -5 -4 10 -5 -5 -5 30 -10

import sys
from collections import deque

n, d = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

q = deque([0])
dp = [-1] * n
dp[0] = lst[0]
for i in range(1, n):
    curMax = dp[q[0]]
    curValue = lst[i] + curMax
    dp[i] = max(curValue, lst[i])

    # 최댓값을 유지하는 작업
    while q and curValue >= dp[q[-1]]:
        q.pop()
    q.append(i)
    
    # 슬라이딩 윈도우 크기 유지
    while q and i - q[0] >= d:
        q.popleft()

# print(dp)
print(max(dp))