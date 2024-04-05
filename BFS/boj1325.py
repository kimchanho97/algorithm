# 5 4
# 3 1
# 3 2
# 4 3
# 5 3

import sys
from collections import  deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

def bfs(node):
    q = deque([node])
    visited = [False] * (n + 1)
    visited[node] = True
    cnt = 0
    while q:
        cn = q.popleft()
        cnt += 1
        for nn in graph[cn]:
            if not visited[nn]:
                q.append(nn)
                visited[nn] = True
    return cnt

result = []
for i in range(1, n+1):
    dp = [-1] * (n + 1)
    result.append(bfs(i))

temp = max(result)
# print(result)
for i, val in enumerate(result):
    if val == temp:
        print(i+1, end=' ')