import sys, heapq

m, n = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().rstrip() for _ in range(n)]
dp = [[float('inf')] * m for _ in range(n)]  # 방향 전환 횟수
visited = [[set() for i in range(m)] for j in range(n)]
# n = row, m = col
for i in range(n):
    for j in range(m):
        if graph[i][j] == "C":
            sr, sc = i, j

def dijkstra(r, c):
    q = [(0, r, c, -1)]
    dp[r][c] = 0
    visited[r][c] = {0, 1, 2, 3}
    while q:
        ccnt, cr, cc, cd = heapq.heappop(q)
        if (cr, cc) != (sr, sc) and graph[cr][cc] == "C":
            return ccnt
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(4):
            nr, nc = cr + move[i][0], cc + move[i][1]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] != "*":
                # 같은 방향
                if cd == i:
                    if ccnt <= dp[nr][nc]:
                        # 횟수가 같을 경우 이전에 방문한 방향이 없는 경우만 탐색
                        if ccnt == dp[nr][nc] and i in visited[nr][nc]:
                            continue

                        heapq.heappush(q, (ccnt, nr, nc, i))
                        dp[nr][nc] = ccnt
                        visited[nr][nc].add(i)
                else:
                    if ccnt + 1 <= dp[nr][nc]:
                        if cd == -1:  # 시작 지점인 경우
                            heapq.heappush(q, (ccnt, nr, nc, i))
                            dp[nr][nc] = ccnt
                            visited[nr][nc].add(i)
                            continue

                        if ccnt + 1 == dp[nr][nc] and i in visited[nr][nc]:
                            continue

                        heapq.heappush(q, (ccnt + 1, nr, nc, i))
                        dp[nr][nc] = ccnt + 1
                        visited[nr][nc].add(i)
    return

print(dijkstra(sr, sc))
# for i in dp:
#     print(i)