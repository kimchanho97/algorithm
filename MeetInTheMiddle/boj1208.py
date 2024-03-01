import sys, bisect
from itertools import combinations

# 배열의 길이 2^20
# 1024 * 1024 = 1_000_000

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
left = arr[:n//2]   # n//2 전까지
right = arr[n//2:]   # n//2 부터

# 부분 수열의 합을 구하는 함수(모든 조합의 합을 구함)
# dp 활용
def get_sum(init_arr):
    sum_arr = [0]
    for num in init_arr:
        new_sum_arr = []
        for i in sum_arr:
            new_sum_arr.append(i + num)
        sum_arr.extend(new_sum_arr)
    sum_arr.remove(0)
    sum_arr.sort()
    return sum_arr

# combinations 활용
def get_sum_combination(init_arr):
    sum_arr = []
    for i in range(1, len(init_arr)+1):
        for comb in combinations(init_arr, i):
            sum_arr.append(sum(comb))
    sum_arr.sort()
    return sum_arr

left_sum = get_sum_combination(left)
right_sum = get_sum_combination(right)

# 부분 수열의 합 경우의 수
# left_sum 에서만 나오는 조합
# right_sum 에서만 나오는 조합
# left_sum + right_sum 에서 나오는 조합

cnt = 0
# print(left_sum, right_sum)
for left_num in left_sum:
    find_num = s - left_num
    left_idx = bisect.bisect_left(right_sum, find_num)
    right_idx = bisect.bisect_right(right_sum, find_num)
    # print(left_num, find_num)
    # print(left_idx, right_idx)
    # print()
    cnt += (right_idx - left_idx)

print(cnt + left_sum.count(s) + right_sum.count(s))