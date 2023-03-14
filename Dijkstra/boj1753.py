import sys, heapq

v, e = map(int, sys.stdin.readline().split())
node = int(sys.stdin.readline())
# 각 지점까지의 distance 'inf'로 초기화
dist = [float('inf')] * (v+1)
graph = [[] for _ in range(v+1)]
for i in range(e):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append([end, weight])

def dijkstra(node):
    dist[node] = 0
    q = []
    heapq.heappush(q, (0, node))
    while q:
        # q에서 가장 cost가 작은 node pop
        cost, curNode = heapq.heappop(q)
        for end, weight in graph[curNode]:
            newCost = cost + weight
            # 최단경로 최신화
            if newCost < dist[end]:
                dist[end] = newCost
                heapq.heappush(q, (newCost, end))
    return

dijkstra(node)

for i in range(1, v+1):
    if dist[i] >= float('inf'):
        print("INF")
    else:
        print(dist[i])