import sys

n, m = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(m)]
dist = [float('inf')] * (n+1)

def bellmanFord(start):
  dist[start] = 0
  for i in range(n):
    for j in range(m):
      s, e, cost = edges[j]
      if dist[s] != float('inf') and dist[s] + cost < dist[e]:
        dist[e] = dist[s] + cost
        # 음의 cycle 존재
        if i == n-1:
          return True
  return False  

if bellmanFord(1):
  print(-1)
else:
  for i in range(2, n+1):
    print(dist[i] if dist[i] != float('inf') else -1)