import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

def dfs(row, col):
    # (row, col)지점에서 도착지까지의 경로의 수
    if row == m - 1 and col == n - 1:
        return 1

    if dp[row][col] != -1:
        return dp[row][col]

    ways = 0
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nextRow = row + dr
        nextCol = col + dc
        if 0 <= nextRow < m and 0 <= nextCol < n and graph[row][col] > graph[nextRow][nextCol]:
            ways += dfs(nextRow, nextCol)

    dp[row][col] = ways
    return dp[row][col]

print(dfs(0, 0))
