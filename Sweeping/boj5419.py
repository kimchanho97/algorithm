# 1
# 6
# -11 10
# -11 -10
# -10 -10
# -10 10
# 10 -10
# 10 10

import sys

def prefixSum(fenwick_tree, i):
    total = 0
    while i >= 1:
        total += fenwick_tree[i]
        i -= (i & -i)
    return total

def update(fenwick_tree, i, diff):
    while i < len(fenwick_tree):
        fenwick_tree[i] += diff
        i += (i & -i)

t = int(sys.stdin.readline())
for test in range(t):
    n = int(sys.stdin.readline())
    dots = []
    temp = []
    idx = dict()
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        dots.append([a, b])
        temp.append(b)

    # y좌표가 작을수록 더 큰 순서를 받는 것
    temp.sort(reverse=True)
    for i, val in enumerate(temp):
        if val in idx:
            continue
        idx[val] = len(idx) + 1

    dots.sort(key=lambda x: (x[0], -x[1]))
    # print(dots)
    for dot in dots:
        dot[1] = idx[dot[1]]
    # print(dots)

    fenwick_tree = [0] * (len(idx)+1)
    answer = 0
    for x, y in dots:
        answer += prefixSum(fenwick_tree, y)
        update(fenwick_tree, y, 1)
    print(answer)