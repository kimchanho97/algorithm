# 3
# 2 2
# 0 1
# 0 0
# 2 3
# 0 1
# 0 0
# 3 3
# 0 1 0
# 0 0 1
# 0 0 0

import sys

def dfs(r, c, dir, cnt, path):
    # 방문 처리 & 경로 추가
    visit[r][c] = True
    path.append((r, c))
    if (r, c) == (n-1, n-1):
        result.append([cnt, path[:]])

    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(4):
        dr, dc = move[i][0], move[i][1]
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 0:
            if not visit[nr][nc]:
                if i == dir:  # 같은 방향
                    dfs(nr, nc, i, cnt, path)
                else:  # 다른 방향(회전)
                    dfs(nr, nc, i, cnt + 1, path)

    visit[r][c] = False
    path.pop()
    return

t = int(sys.stdin.readline())
for test in range(t):
    n, k = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    result = []

    dfs(0, 0, 0, 0, [])  # 동쪽 방향 시작
    result.append((-1, -1))
    dfs(0, 0, 1, 0, [])  # 남쪽 방향 시작

    flag = False
    for i in result:
        print(i)
        if i[0] == k:
            flag = True
    print(flag)

