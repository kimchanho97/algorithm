import sys, heapq

n = int(sys.stdin.readline())
lecture = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lecture.sort()
# print(lecture)
endTime = [0]

for s, e in lecture:
    earliest = endTime[0]
    # 현재 강의실 중 가장 빨리 종료되는 시각
    if s >= earliest:
        heapq.heappop(endTime)
    heapq.heappush(endTime, e)
    # print(endTime)
print(len(endTime))