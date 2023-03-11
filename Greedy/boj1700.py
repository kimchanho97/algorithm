import sys, heapq

n, k = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
# n = 100, k = 100
cnt = 0
multitap = []
for i in range(k):
    newThing = seq[i]
    if newThing not in multitap:
        if len(multitap) < n:
            multitap.append(newThing)

        else:
            heap = []
            for j in range(n):
                oldThing = multitap[j]
                pivot = k
                # pivot: 우선순위(처음 사용되는 위치), k: 가장 마지막 위치
                for l in range(i+1, k):
                     # 이후에 처음으로 사용되는 위치를 기준으로 우선순위를 준다
                    if oldThing == seq[l]:
                        pivot = l
                        break
                heapq.heappush(heap, (-pivot, j))  # j: 멀티탭 위치

            firstUsePos, oldThingPos = heapq.heappop(heap)
            multitap[oldThingPos] = newThing
            cnt += 1

print(cnt)