import sys

def floydWarshall():
  # 가장 외곽 for문: 우회하는 node 번호
  for k in range(1, n+1):
    for i in range(1, n+1):
      for j in range(1, n+1):          
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dist = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for i in range(m):
  s, e, cost = map(int, sys.stdin.readline().split(' '))
  dist[s][e] = min(cost, dist[s][e])

for i in range(n+1):
  dist[i][i] = 0
floydWarshall()
for i in range(1, n+1):
  for j in range(1, n+1):
    print(dist[i][j] if dist[i][j] != sys.maxsize else 0, end=' ')
  print()