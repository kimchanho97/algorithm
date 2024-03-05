import sys

n = int(sys.stdin.readline())
w = int(sys.stdin.readline())
arr = [(0, 0)]
arr.extend([tuple(map(int, sys.stdin.readline().split())) for _ in range(w)])

dp = [[float('inf')] * (w+1) for _ in range(w+1)]
dp[0][0] = 0

def dist(a, b, car):
    r1, c1 = arr[a]
    if b == 0:
        if car == 1:
            r2, c2 = (1, 1)
        elif car == 2:
            r2, c2 = (n, n)
    else:
        r2, c2 = arr[b]
    return abs(r1 - r2) + abs(c1 - c2)

dp[1][0] = dist(1, 0, 1)
dp[0][1] = dist(1, 0, 2)

trace = [[-1] * (w+1) for _ in range(w+1)]
trace[1][0] = (0, 0)
trace[0][1] = (0, 0)

for i in range(w+1):
    for j in range(i): # 항상 j < i
        # dp[i][j], dp[j][i] 정의
        if i - j == 1:
            for k in range(i-1):
                if dp[k][j] + dist(i, k, 1) < dp[i][j]:
                    dp[i][j] = dp[k][j] + dist(i, k, 1)
                    trace[i][j] = (k, j)
                if dp[j][k] + dist(i, k, 2) < dp[j][i]:
                    dp[j][i] = dp[j][k] + dist(i, k, 2)
                    trace[j][i] = (j, k)

        else: # i > 2
            dp[i][j] = dp[i-1][j] + dist(i, i-1, 1)
            trace[i][j] = (i-1, j)
            dp[j][i] = dp[j][i-1] + dist(i, i-1, 2)
            trace[j][i] = (j, i-1)

result = float('inf')
r, c = 0, 0
for i in range(w+1):
    if dp[w][i] < result:
        result = dp[w][i]
        r, c = w, i
    if dp[i][w] < result:
        result = dp[i][w]
        r, c = i, w

seq = []
while trace[r][c] != -1:
    nr, nc = trace[r][c]
    if c == nc:
        seq.append(1)
    else:
        seq.append(2)
    r, c = nr, nc
seq.reverse()

print(result)
for num in seq:
    print(num)