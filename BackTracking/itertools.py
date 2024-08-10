from itertools import combinations, permutations, product

nums = [1, 2, 3]
n = len(nums)

result = []
lst = []
# 순열 직접 구현
def myPermutation():
    used = [False] * n
    def permutate(idx, length):
        if idx == length:
            result.append(tuple(lst[:]))
            return

        for i in range(n):
            if not used[i]:
                used[i] = True
                lst.append(nums[i])
                permutate(idx + 1, length)
                lst.pop()
                used[i] = False
        return

    for i in range(1, n + 1):
        permutate(0, i)

myPermutation()
print(result)

result = []
lst = []
# 조합 직접 구현
def myCombination(idx):
    if idx == n:
        if lst:
            result.append(tuple(lst[:]))
        return

    lst.append(nums[idx])
    myCombination(idx + 1)
    lst.pop()
    myCombination(idx + 1)
    return

myCombination(0)
print(result)

result = []
lst = []
# 중복순열 직접 구현
def myProduct():
    def getProduct(idx, length):
        if idx == length:
            result.append(tuple(lst[:]))
            return

        for i in range(n):
            lst.append(nums[i])
            getProduct(idx + 1, length)
            lst.pop()
        return
    for i in range(1, n + 1):
        getProduct(0, i)

myProduct()
print(result)
print()

per_result = []
com_result = []
pro_result = []
for i in range(1, n+1):
    per_result.extend(list(permutations(nums, i)))
    com_result.extend(list(combinations(nums, i)))
    pro_result.extend(list(product(nums, repeat = i)))
print(per_result)
print(com_result)
print(pro_result)