import sys, heapq

n = int(sys.stdin.readline())  # 10,000
k = int(sys.stdin.readline())  # 1,000
sensor = list(map(int, sys.stdin.readline().split()))  # 1,000,000
sensor.sort()
# print(sensor)

# 핵심: 센서를 등분하는 갓
# 1 3 / 6 7 9
# 가장 거리 차이가 멀리 나는 지점을 등분/ 거리차가 큰 지점은 합계에서 제외

heap = []
for i in range(n-1):
    heapq.heappush(heap, -(sensor[i+1] - sensor[i])) # 각 지점의 거리차

if k > n:
    print(0)
else:
    for i in range(k-1):
        heapq.heappop(heap)
    print(-sum(heap))

