## [골드1]구간 합 구하기(http://www.acmicpc.net/problem/2042)

### 세그먼트 트리:

- 구간의 정보를 가지고 있는 트리(구간 합, 구간 내 최댓값, 최솟값 등)
- N개의 쿼리가 들어올 경우 -> O(NlogN)
  <br>
  <img src="https://mblogthumb-phinf.pstatic.net/20160819_75/kks227_147161282094442Rpc_PNG/1.png?type=w800" width="600">

* 트리 선언

  ```python
  lst = [0]
  for i in range(n):
      num = int(sys.stdin.readline())
      lst.append(num)

  nodeNum = 2 ** (math.ceil(math.log(n, 2))+1)
  tree = [0] * nodeNum
  ```

- 트리 초기화(makeTree)

  ```python
  def makeTree(node, start, right):
      if start == right:
          tree[node] = lst[start]
          return tree[node]
      mid = (start + right) // 2
      tree[node] = makeTree(node*2, start, mid) + makeTree(node*2+1, mid+1, right)
      return tree[node]

  makeTree(1, 1, n)
  ```

* 구간 합 구하기(getSum)

  ```python
  def getSum(node, start, end, left, right):
      # left, right = 구하고자 하는 범위
      if left <= start and end <= right:
          return tree[node]
      if start > right or end < left:
          return 0
      mid = (start+end)//2
      return getSum(node*2, start, mid, left, right) + getSum(node*2+1, mid+1, end, left, right)

  getSum(1, 1, n, l, r)
  ```

  - start와 end는 정해져 있는 각 세그먼트 트리의 구간으로 만약 left, right안에 들어올 경우 tree[node]를 리턴한다.

* 원소 값 교체(update)

  ```python
  def update(node, start, end, idx, value):
    if idx < start or idx > end:
        return

    tree[node] += value
    if start == end:
        return

    mid = (start + end) // 2
    update(node*2, start, mid, idx, value)
    update(node*2+1, mid+1, end, idx, value)
    return
  ```

  - start와 end는 세그먼트 트리의 정해진 구간으로 idx가 구간 밖에 있을 경우 return한다.
  - `makeTree`함수 없이 `update`만으로도 트리 구현이 가능하다. -> 초기 배열의 원소를 하나씩 update
  - **중요!!: 값을 갱신한 이후 리프node의 값을 저장하는 배열 lst역시 갱신해주어야 한다.**

<br>
