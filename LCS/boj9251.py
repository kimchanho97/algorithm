import sys

short = sys.stdin.readline().strip()
long = sys.stdin.readline().strip()

n = len(short)
m = len(long)
dp = [[0] * (m+1) for _ in range(n+1)]
# dp[i][j] : short[:i]와 long[:j]의 최대 공통 부분 수열의 길이
for i in range(1, n+1):
    for j in range(1, m+1):
        if short[i-1] == long[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[n][m])