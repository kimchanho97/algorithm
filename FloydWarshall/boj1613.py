import sys

def floydWarshall():
  for k in range(1, n+1):
    for i in range(1, n+1):
      for j in range(1, n+1):
        if dist[i][k] != 0 and dist[i][k] == dist[k][j]:
          dist[i][j] = dist[i][k]

n, m = map(int ,sys.stdin.readline().split())
dist = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
  s, e = map(int, sys.stdin.readline().split())
  dist[s][e] = -1
  dist[e][s] = 1

floydWarshall()
k = int(sys.stdin.readline())
for i in range(k):
  s, e = map(int, sys.stdin.readline().split())
  print(dist[s][e])