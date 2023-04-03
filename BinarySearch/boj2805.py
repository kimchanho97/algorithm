import sys

#  n = 나무개수, m = 가져가려는 나무의 길이
n, m = map(int, sys.stdin.readline().split()) 
trees = list(map(int, sys.stdin.readline().split()))

def getLength(height):
    total = 0
    for tree in trees:
        if tree > height:
            total += (tree - height)
    return total

start = 0
end = max(trees)
result = 0
while start <= end:
    mid = (start + end) // 2
    length = getLength(mid)
    if length >= m:
        # 가져갈 수 있는 경우에 대한 마지막 mid값
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)