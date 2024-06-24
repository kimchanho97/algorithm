# 10 15
# 5 1 3 5 10 7 4 9 2 8

import sys

n, s = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

l, r = 0, 0
temp = 0
answer = sys.maxsize
# l부터 r-1 까지의 합
while True:
    if temp < s:
        if r == n:
            break
        temp += lst[r]
        r += 1
    else:
        answer = min(r - l, answer)
        temp -= lst[l]
        l += 1

print(answer if answer != sys.maxsize else 0)