import sys
from collections import deque


def topology_sort(node):
    q = deque([node])
    while q:
        curNode = q.popleft()
        for nextNode, cost in graph[curNode]:
            dp[nextNode] = max(dp[nextNode], dp[curNode] + cost)
            indegree[nextNode] -= 1
            if indegree[nextNode] == 0:
                q.append(nextNode)


def bfs(node):
    q = deque([(node, 0)])
    while q:
        curNode, curSum = q.popleft()
        for nextNode, cost in graph[curNode]:
            if dp[nextNode] > curSum + cost:
                continue
            q.append((nextNode, curSum + cost))
            dp[nextNode] = curSum + cost


def dfs(node, sum):
    dp[node] = max(dp[node], sum)
    for nextNode, cost in graph[node]:
        if sum + cost > dp[nextNode]:
            dfs(nextNode, sum + cost)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
reversedGraph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1)
for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((e, c))
    reversedGraph[e].append((s, c))
    indegree[e] += 1

start, end = map(int, sys.stdin.readline().split())
dp = [0] * (n+1)

topology_sort(start)
# dfs(start, 0)
# bfs(start)
# print(dp)

def trace(node):
    q = deque([node])
    visit[node] = True
    cnt = 0
    while q:
        curNode = q.popleft()
        for nextNode, cost in reversedGraph[curNode]:
            if dp[curNode] - cost == dp[nextNode]:
                cnt += 1
                if not visit[nextNode]:
                    q.append(nextNode)
                    visit[nextNode] = True
    return cnt

print(dp[end])
visit = [False] * (n+1)
print(trace(end))