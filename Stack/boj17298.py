import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = []
result = [-1] * n
for i, val in enumerate(arr):
    if len(stack) == 0:
        stack.append(i)
    else:
        if val > arr[stack[-1]]:
            while len(stack) > 0 and val > arr[stack[-1]]:
                idx = stack.pop()
                result[idx] = val
        stack.append(i)

for i in result:
    print(i, end=' ')