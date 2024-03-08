import sys, heapq, math

def find(n):
    if p[n] < 0:
        return n
    else:
        p[n] = find(p[n])
        return p[n]

def merge(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        p[root_a] += p[root_b]
        p[root_b] = root_a
        return True
    return False

n, m = map(int, sys.stdin.readline().split())
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
conn = set()
p = [-1] * n

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    conn.add((a-1, b-1))

dist = []
for i in range(n):
    for j in range(i + 1, n):
        if (i, j) in conn or (j, i) in conn:
            merge(i, j)

        else:
            x1, y1 = dots[i]
            x2, y2 = dots[j]
            dist.append(((math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)), i, j))

dist.sort()

result = 0
while dist:
    cost, a, b = heapq.heappop(dist)
    if merge(a, b):
        result += cost

print(f'{result:.2f}')  # f-string은 반올림 한 값을 출력.