import sys

n, m = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * (m+1) for _ in range(n+1)]

# 전처리
for i in range(1, n+1):
    for j in range(1, m+1):
        # dp[i][j] = (0, 0)과 (i, j)을 대각선으로 가지는 사각형의 넓이
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]

k = int(sys.stdin.readline())
for i in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(dp[c][d] - dp[c][b-1] - dp[a-1][d] + dp[a-1][b-1])