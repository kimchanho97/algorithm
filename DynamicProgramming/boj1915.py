# 6 6
# 111011
# 111111
# 111111
# 001111
# 111111
# 111111

import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
dp = [[[0, 0] for i in range(m+1)] for j in range(n+1)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dp[i+1][j+1][1] = dp[i][j+1][1] + 1
            dp[i+1][j+1][0] = dp[i+1][j][0] + 1

# for i in dp:
    # print(i)

answer = [[0] * (m+1) for _ in range(n+1)]
result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        length = min(dp[i][j])
        if length > answer[i-1][j-1]:
            answer[i][j] = answer[i-1][j-1] + 1
        else:
            answer[i][j] = length
        result = max(result, answer[i][j])

# for i in answer:
    # print(i)

print(result ** 2)