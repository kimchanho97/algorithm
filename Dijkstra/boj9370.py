import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [int(1e9)] * (n + 1)
    q = [(0, start)]
    distance[start] = 0
    while q:
        cost, curNode = heapq.heappop(q)
        for nextNode, c in graph[curNode]:
            if cost + c < distance[nextNode]:
                distance[nextNode] = cost + c
                heapq.heappush(q, (cost+c, nextNode))
    return distance

t = int(input())
for k in range(t):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a, b) == (g, h) or (a, b) == (h, g):
            distGH = d
    nodes = [int(input()) for _ in range(t)]
    nodes.sort()
    distFromS = dijkstra(s)
    distFromG = dijkstra(g)
    distFromH = dijkstra(h)
    # 경로
    # case1 = s -> (...) -> g -> h -> (...) -> node
    # case2 = s -> (...) -> h -> g -> (...) -> node
    for node in nodes:
        if (distFromS[node] == distFromS[g] + distGH + distFromH[node]) or (distFromS[node] == distFromS[h] + distGH + distFromG[node]):
            print(node, end=' ')
    print()