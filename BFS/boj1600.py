# 7
# 7 7
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0

import sys
from collections import deque

def bfs(r, c):
    q = deque([(0, k, r, c)])
    visit = [[-1] * m for _ in range(n)]
    visit[r][c] = k
    while q:
        cnt, jump, curR, curC = q.popleft()
        if curR == n-1 and curC == m-1:
            return cnt

        horse = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        if jump > 0:
            for dr, dc in horse:
                nr, nc = curR + dr, curC + dc
                if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0 and jump-1 > visit[nr][nc]:
                    q.append((cnt+1, jump-1, nr, nc))
                    visit[nr][nc] = jump-1

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = curR + dr, curC + dc
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0 and jump > visit[nr][nc]:
                q.append((cnt+1, jump, nr, nc))
                visit[nr][nc] = jump

    return -1

k = int(sys.stdin.readline())
m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(bfs(0, 0))