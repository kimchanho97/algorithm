# 6 3
# 3 1 4 3
# 4 6 2 5 4
# 2 2 3

import sys
from collections import deque

def topology_sort(indegree, graph):
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    for i in range(n):
        if not q:
            return [0]

        cur = q.popleft()
        result.append(cur)
        for next in graph[cur]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    return result

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    seq = list(map(int, sys.stdin.readline().split()))[1:]
    for i in range(len(seq) - 1):
        s = seq[i]
        e = seq[i + 1]
        graph[s].append(e)
        indegree[e] += 1

# print(graph)
# print(indegree)
answer = topology_sort(indegree, graph)
for i in answer:
    print(i)