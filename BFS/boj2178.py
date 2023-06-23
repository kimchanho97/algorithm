import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

def bfs():
  q = deque([(1, 0, 0)])
  visit[0][0] = 1
  while q:
    cnt, row, col = q.popleft()
    if row == n-1 and col == m-1:
      return cnt
      
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
      nextRow, nextCol = row+dr, col+dc
      if 0 <= nextRow < n and 0 <= nextCol < m:
        if graph[nextRow][nextCol] == 1 and not visit[nextRow][nextCol]:
          visit[nextRow][nextCol] = cnt+1
          q.append((cnt+1, nextRow, nextCol))
  return 
    
print(bfs())