import sys, math

def makeTree(node, start, right):
    if start == right:
        tree[node] = lst[start]
        return tree[node]
    mid = (start + right) // 2
    tree[node] = makeTree(node*2, start, mid) + makeTree(node*2+1, mid+1, right)
    return tree[node]

# getSum(1, 1, 5, 1, 4)
# getSum(1, 1, 3, 1, 4) + getSum(1, 4, 5, 1, 4)
# getSum(1, 1, 3, 1, 4) + getSum(1, 4, 4, 1, 4) + getSum(1, 5, 5, 1, 4)
def getSum(node, start, end, left, right):
    # start, end = 시작, 끝
    # left, right = 구하고자 하는 범위

    # 시작과 끝이 구하고자 하는 범위 안
    if left <= start and end <= right:
        return tree[node]
    if start > right or end < left:
        return 0
    mid = (start+end)//2
    return getSum(node*2, start, mid, left, right) + getSum(node*2+1, mid+1, end, left, right)


def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start+end)//2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)
    return

n, m, k = map(int ,sys.stdin.readline().split())
lst = [0]
for i in range(n):
    num = int(sys.stdin.readline())
    lst.append(num)

nodeNum = 2 ** (math.ceil(math.log(n, 2))+1)
tree = [0] * nodeNum

makeTree(1, 1, n)

for i in range(m+k):
    comm, l, r = map(int, sys.stdin.readline().split())
    if int(comm) == 1:
        idx, value = l, r
        diff = value - lst[idx]
        lst[idx] = value
        update(1, 1, n, idx, diff)
    else:
        print(getSum(1, 1, n, l, r))