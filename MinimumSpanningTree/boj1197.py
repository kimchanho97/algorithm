import sys, heapq

n, m = map(int, sys.stdin.readline().split())
edges = []
for i in range(m):
    s, e, c = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(edges, ((c, s, e)))

p = [-1] * (n+1)

def find(n):
    if p[n] < 0:
        return n
    else:
        p[n] = find(p[n])
        return p[n]

def merge(a, b):
    p[a] += p[b]
    p[b] = a

result = 0
cnt = 0 # 간선의 개수
while cnt < n-1: # 최소 스패닝 트리의 간선의 개수는 n-1이다.
    cost, a, b = heapq.heappop(edges)
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        result += cost
        cnt += 1
        merge(root_a, root_b)

print(result)