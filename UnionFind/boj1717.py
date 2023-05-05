import sys

n, m = map(int, sys.stdin.readline().split())
p = [-1] * (n+1)

def find(n):
    if p[n] < 0:
        return n
    else:
        p[n] = find(p[n])
        # 바로 root를 가리키도록 이어줌
        return p[n]

def merge(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        p[rootA] += p[rootB]
        p[rootB] = rootA
    return

for i in range(m):
    command, l, r = map(int ,sys.stdin.readline().split())
    if command == 0:
        merge(l, r)

    else:
        rootL = find(l)
        rootR = find(r)
        if rootL == rootR:
            print("YES")
        else:
            print("NO")
