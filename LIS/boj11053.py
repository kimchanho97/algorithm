import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * n
for i, num in enumerate(arr):
    for j, before_num in enumerate(arr[:i+1]):
        if num > before_num:
            dp[i] = max(dp[j]+1, dp[i])
# print(dp)
print(max(dp))