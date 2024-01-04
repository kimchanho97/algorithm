import sys

t = int(sys.stdin.readline())
# k 500 이하
for i in range(t):
    k = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * (k + 1) for _ in range(k + 1)]
    psum = [0] * (k + 1)
    for i in range(1, k + 1):
        psum[i] = psum[i - 1] + files[i - 1]
    for i in range(1, k):
        dp[i][i + 1] = files[i - 1] + files[i]

    for i in range(k, 0, -1):
        for j in range(k + 1):
            # 무조건 j > i
            if j <= i:
                continue
            dp[i][j] = min([(dp[i][k] + dp[k + 1][j])
                           for k in range(i, j)]) + (psum[j] - psum[i - 1])

    print(dp[1][k])
