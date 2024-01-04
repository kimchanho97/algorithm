import sys
import heapq

t = int(sys.stdin.readline())
# k 500 이하
for i in range(t):
    k = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(files)
    total = 0
    while len(files) > 1:
        left = heapq.heappop(files)
        right = heapq.heappop(files)
        total += (left + right)
        # print(left, right, total)
        heapq.heappush(files, left + right)
    print(total)
