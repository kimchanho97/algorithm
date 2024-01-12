import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bytes = list(map(int, input().split()))
costs = list(map(int, input().split()))
arr = [(costs[i], bytes[i]) for i in range(n)]
arr.sort(key=lambda x: (x[0], x[1]))
MAX_LEN = sum(costs)
dp = [[0] * (MAX_LEN+1) for _ in range(n+1)]

# 냅색 알고리즘
for i in range(1, n+1):
    cost, byte = arr[i-1]
    for j in range(0, MAX_LEN+1):
        if j >= cost:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-cost] + byte, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# for i in dp:
    # print(i)
            
for i, val in enumerate(dp[n]):
    if val >= m:
        print(i)
        break