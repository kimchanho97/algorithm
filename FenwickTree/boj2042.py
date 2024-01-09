# 2042번(구간 합 구하기)
# 시간제한: 2초
# 펜윅 트리(Fenwick Tree)
# 마지막 비트를 활용한 트리구조
# 0이 아닌 마지막 비트 = 내가 저장하고 있는 값들의 개수
import sys

# 데이터의 개수(n), 변경 횟수(m), 구간 합 계간 횟수(k)
# 데이터 변경, 구간 합 계산 -> O(logN)
n, m, k = map(int, sys.stdin.readline().split())
lst = [0] * (n+1)
tree = [0] * (n+1)

# i번째 수를 diff만큼 더하는 함수
def update(i, diff):
    # example)
    # 3 = 0011
    # 3 -> 4 -> 8 -> 16(3의 합의 정보를 가지고 있는 항)
    while i <= n:
        tree[i] += diff
        i += (i & -i)

def prefixSum(i):
    # 1 부타 i까지의 합을 구함(lst)
    # example)
    # 1 ~ 7: 7 -> 6(5와6의 합) -> 4(1 ~ 4합)
    sum = 0
    while i > 0:
        sum += tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 이동
        i -= (i & -i)
    return sum

def getSum(left, right):
    return prefixSum(right) - prefixSum(left-1)

# 배열과 트리 초기화
for i in range(1, n+1):
    num = int(sys.stdin.readline())
    lst[i] = num
    update(i, num)

# 입력에 대한 처리
for i in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1: # update
        diff = c - lst[b]
        update(b, diff)
        lst[b] = c
    if a == 2: # sum
        print(getSum(b, c))