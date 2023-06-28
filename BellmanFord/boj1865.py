import sys

INF = sys.maxsize

def bellmanFord():
  # 음의 Cycle 존재 여부만 확인
  for i in range(n):
    for j in range(len(edges)):
      s, e, cost = edges[j]
      if dist[s] + cost < dist[e]:
        # print(dist[s], cost, dist[e], i, j)
        dist[e] = dist[s] + cost
        # 음의 Cycle 존재
        if i == n-1:
          return True
  return False

t = int(sys.stdin.readline())
for _ in range(t):
  n, m, w = map(int, sys.stdin.readline().split())
  edges = []
  for i in range(m):
    s, e, cost = map(int, sys.stdin.readline().split(' '))
    edges.append([s, e, cost])
    edges.append([e, s, cost])
  for i in range(w):
    s, e, cost = map(int, sys.stdin.readline().split(' '))
    edges.append([s, e, -cost])

  dist = [INF] * (n+1)
  print('YES' if bellmanFord() else 'NO')