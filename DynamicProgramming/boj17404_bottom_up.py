import sys

n = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[float('inf')] * 3 for _ in range(n + 1)]

R, G, B = 0, 1, 2
result = float('inf')
for i in range(3):
    dp[1] = [float('inf'), float('inf'), float('inf')]
    dp[1][i] = cost[0][i]

    for j in range(2, n + 1):
        dp[j][R] = cost[j - 1][R] + min(dp[j - 1][G], dp[j - 1][B])
        dp[j][G] = cost[j - 1][G] + min(dp[j - 1][R], dp[j - 1][B])
        dp[j][B] = cost[j - 1][B] + min(dp[j - 1][R], dp[j - 1][G])

    # for s in dp:
    #     print(s)
        
    dp[n][i] = float('inf')
    result = min(result, min(dp[n]))

print(result)