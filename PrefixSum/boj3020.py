import sys

n, h = map(int, sys.stdin.readline().split())
top = [0] * (h+1)
bottom = [0] * (h+1)

for i in range(n):
    height = int(sys.stdin.readline())
    if i % 2 == 0:
        bottom[height] += 1
    else:
        top[height] += 1

# prefix
for i in range(h-1, 0, -1):
    top[i] = top[i+1] + top[i]
    bottom[i] = bottom[i+1] + bottom[i]

result = []
for i in range(1, h+1):
    result.append(bottom[i] + top[-i])
    
print(min(result), result.count(min(result)))