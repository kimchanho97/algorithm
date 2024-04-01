import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[[-1] * 3 for i in range(3)] for j in range(n)]

def dfs(row, col, start):
    # dp[row][col][start]: row, col을 포함하며, 시작점이 start일때, 남은 경로를 완성하는 최소비용
    if row == n - 1:
        if col == start:
            dp[row][col][start] = float('inf')
        else:
            dp[row][col][start] = cost[row][col]
        return dp[row][col][start]

    if dp[row][col][start] != -1:
        return dp[row][col][start]

    temp = float('inf')
    for i in range(3):
        if col == i:
            continue
        temp = min(temp, cost[row][col] + dfs(row + 1, i, start))
    dp[row][col][start] = temp
    return dp[row][col][start]

result = [dfs(0, 0, 0), dfs(0, 1, 1), dfs(0, 2, 2)]

# for i in dp:
    # print(i)

print(min(result))