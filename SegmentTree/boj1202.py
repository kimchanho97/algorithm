# 9 5
# 4 5
# 4 9
# 4 10
# 7 55
# 14 20
# 9 15
# 8 55
# 8 5
# 11 54
# 10
# 5
# 4
# 15
# 20

import sys, math
import bisect

def initTree(node, start, end):
    if start == end:
        tree[node] = (lst[start], start)
        return tree[node]

    mid = (start + end) // 2
    left_value, left_index = initTree(node*2, start, mid)
    right_value, right_index = initTree(node*2+1, mid+1, end)
    if left_value <= right_value:
        tree[node] = (left_value, left_index)
    else:
        tree[node] = (right_value, right_index)
    return tree[node]

def update(node, start, end, idx, value):
    if idx < start or idx > end:
        return tree[node]
    if start == end:
        tree[node] = (value, idx)
        return tree[node]

    mid = (start + end) // 2
    left_value, left_index = update(node * 2, start, mid, idx, value)
    right_value, right_index = update(node * 2 + 1, mid + 1, end, idx, value)
    if left_value <= right_value:
        tree[node] = (left_value, left_index)
    else:
        tree[node] = (right_value, right_index)
    return tree[node]

def getMin(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node]
    if left > end or right < start:
        return float('inf'), -1

    mid = (start + end) // 2
    left_value, left_index = getMin(node*2, start, mid, left, right)
    right_value, right_index = getMin(node*2+1, mid+1, end, left, right)
    if left_value <= right_value:
        return left_value, left_index
    else:
        return right_value, right_index

n, k = map(int, sys.stdin.readline().split())
items = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: -x[1])
bag = sorted(int(sys.stdin.readline()) for _ in range(k))
lst = [0] * k
nodes = 1 << math.ceil(math.log2(k) + 1)
tree = [-1] * nodes
initTree(1, 0, k-1)
for weight, price in items:
    if weight > bag[-1]:
        continue
    idx = bisect.bisect_left(bag, weight)
    minValue, minIdx = getMin(1, 0, k-1, idx, k-1)
    if price > minValue:
        update(1, 0, k-1, minIdx, price)
        lst[minIdx] = price

# print(items)
# print(bag)
# print(lst)
print(sum(lst))