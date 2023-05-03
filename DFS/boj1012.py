import sys
sys.setrecursionlimit(10**6)

def dfs_recursion(y, x):
    visit[y][x] = True
    move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for dy, dx in move:
        if 0 <= y + dy < n and 0<= x + dx < m:
            # 방문여부와 배추가 있는지 확인
            if not visit[y+dy][x+dx] and vege[y+dy][x+dx]:
                dfs_recursion(y+dy, x+dx)

def dfs_stack(y, x):
    visit[y][x] = True
    stack = [(y, x)]
    move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while stack:
        now_y, now_x = stack.pop()
        for dy, dx in move:
            next_y, next_x = now_y+dy, now_x+ dx
            # 방문여부와 배추 확인
            if 0 <= next_y < n and 0<= next_x < m:
                if not visit[next_y][next_x] and vege[next_y][next_x]:
                    # 첫 방문일 경우: 방문처리, stack추가(해당지점으로 이동)
                    visit[next_y][next_x] = True
                    stack.append((next_y, next_x))


t = int(sys.stdin.readline())
for _ in range(t):
    # m = 가로, n = 세로, k = 위치의 개수
    m, n, k = map(int, sys.stdin.readline().split())

    vege = [[0] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        vege[y][x] = 1

    res = 0
    for y in range(n):
        for x in range(m):
           if vege[y][x] and not visit[y][x]:
               dfs_stack(y, x)
               res += 1
    print(res)