import sys

n, goal = map(int ,sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
cnt = 0
def getSum(total, idx):
    global cnt
    if idx < n:
        getSum(total + seq[idx], idx+1)
        getSum(total, idx+1)
        if (total + seq[idx]) == goal:
            cnt += 1
    return

getSum(0, 0)
print(cnt)