import sys
input = sys.stdin.readline

n = int(input()) # 30이하
weights = list(map(int, input().split()))
m = int(input()) # 7이하
arr = list(map(int, input().split()))

MAX_WEIGHT = 40_000 # 구슬의 최대 무게
dp = [[False] * (MAX_WEIGHT + 1) for _ in range(n+1)]

for i in range(1, n+1):
    weight = weights[i-1]
    dp[i][weight] = True
    for j in range(1, MAX_WEIGHT+1):
        if dp[i-1][j]: # True
            dp[i][j] = True
            if weight - j >= 1: # j가 작은 경우
                dp[i][weight-j] = True
            else: # j가 더 큰 경우
                dp[i][j-weight] = True
            if weight + j <= MAX_WEIGHT:
                dp[i][weight+j] = True

for ballWeight in arr:
    print("Y" if dp[n][ballWeight] else "N", end=' ')