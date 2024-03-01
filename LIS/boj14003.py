import bisect, sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

lst = []  # 실제 값이 저장될 리스트
indexes = []  # lst 배열의 각 원소가 arr에서 어떤 인덱스에 해당하는지 저장
p = [-1] * len(arr)  # 각 원소가 LIS에 추가될 때의 '이전 원소 인덱스'를 저장

for i, num in enumerate(arr):
    if not lst:
        lst.append(num)
        indexes.append(i)
    else:
        if num > lst[-1]:
            lst.append(num)
            p[i] = indexes[-1]
            indexes.append(i)
        else:
            idx = bisect.bisect_left(lst, num)
            lst[idx] = num
            indexes[idx] = i
            # i보다 작은 인덱스 중 가장 큰 인덱스를 찾아서 p[i]에 저장
            if idx > 0: # idx가 0이면 이전 원소가 없으므로 p[i] = -1
                p[i] = indexes[idx -1]

# print(arr)
# print(p)
# print(indexes)

idx = indexes[-1]
result = []
while p[idx] != -1:
    result.append(arr[idx])
    idx = p[idx]
result.append(arr[idx])
result.reverse()
print(len(result))
print(' '.join(map(str, result)))