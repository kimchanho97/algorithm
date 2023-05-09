import sys

n, m = map(int, sys.stdin.readline().split())
dp = [[float('inf')] * (m+1) for _ in range(n+1)]

time = []
for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    time.append(lst)

for i in range(n+1):
    dp[i][0] = 0
for i in range(m+1):
    dp[0][i] = 0

# dp[i][j]: 마지막으로 j번째 무기를 사용하고 i회차까지의 최소 시간
for i in range(1, n+1):
    for j in range(1, m+1):
        # 이전 회차에서 j번째가 아닌 시간중 최소 시간 + j번째 무기의 클리어 시간
        for k in range(1, m+1):
            dp[i][j] = min(dp[i][j], dp[i-1][k] + time[i-1][j-1]) if k != j else dp[i][j]

print(min(dp[n][1:m+1]))