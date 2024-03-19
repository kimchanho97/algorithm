import sys

n = int(sys.stdin.readline())
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n)]

for i in range(1, 10):
    dp[0][i][(1 << i)] = 1

# bottom-up
# i = 자리수, k = 마지막 숫자, j = state
for i in range(n-1):
    for k in range(10):
        for j in range(1<<10):
            if dp[i][k][j] != 0:
                if k == 0:
                    dp[i+1][1][j|(1<<1)] += dp[i][k][j]
                elif k == 9:
                    dp[i+1][8][j|(1<<8)] += dp[i][k][j]
                else:
                    dp[i+1][k-1][j|(1<<(k-1))] += dp[i][k][j]
                    dp[i+1][k+1][j|(1<<(k+1))] += dp[i][k][j]

total = 0
for i in range(10):
    total += dp[n-1][i][(1<<10)-1]
    
print(total % 1_000_000_000)