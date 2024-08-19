# 5 3
# 1 101
# 2 99
# 5 90
# 1 65
# 5 23
# 2
# 4
# 10

import sys, heapq

n, m = map(int, sys.stdin.readline().split())
jews = sorted(tuple(map(int, sys.stdin.readline().split())) for _ in range(n))
bags = sorted(int(sys.stdin.readline()) for _ in range(m))

result = 0
pocket = []
for bag in bags:
    while jews and jews[0][0] <= bag:
        weight, price = heapq.heappop(jews)
        heapq.heappush(pocket, -price)

    if pocket:
        result -= (heapq.heappop(pocket))
print(result)