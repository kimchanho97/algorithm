import sys

n = int(sys.stdin.readline())
# s: 시작 시각, e: 종료 시각(1<=s<=e<=1000000)
prefix = [0] * 1000002
# 시작과 끝 쿼리 처리
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    prefix[s] += 1
    prefix[e+1] -= 1

# 누적합 
for i in range(1, 1000001):
    prefix[i] = prefix[i-1] + prefix[i]

m = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    temp = lst[i]
    print(prefix[temp])