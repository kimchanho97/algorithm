import sys, bisect

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

lst = [0]
for i, num in enumerate(arr):
    if num > lst[-1]:
        lst.append(num)
    else:
        idx = bisect.bisect_left(lst, num)
        lst[idx] = num
print(len(lst) -1)