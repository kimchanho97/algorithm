import sys

n = int(sys.stdin.readline())
lst = sorted(map(int, sys.stdin.readline().split()))
# print(lst)

l, r = 0, n-1
diff = abs(lst[l] + lst[r])
left, right = lst[l], lst[r]
while l < r:
    num = lst[l] + lst[r]
    print(f"{lst[l]} + {lst[r]} = {num}")
    if abs(num) < diff:
        diff = abs(num)
        left, right = lst[l], lst[r]

    if num < 0:
        l += 1
    elif num == 0:
        break
    else:
        r -= 1

print(left, right)