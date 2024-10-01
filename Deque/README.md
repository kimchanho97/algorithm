## [플래5]연세워터파크(http://www.acmicpc.net/problem/15678)

- 문제: 배열과 배열의 길이보다 작은 슬라이딩 윈도우의 크기가 주어진다. 0번 인덱스부터 순회하면서 슬라이딩 윈도우 내 최댓값을 찾는 문제

* 알고리즘: `덱을 이용한 구간 최댓값 트릭`

* 해설: 배열의 길이를 n이고 슬라이딩 윈도우의 크기를 m일 때, 각각의 원소를 순회하면서 슬라이딩 윈도우의 최댓값을 구하려면 단순하게 생각하면 O(n x m)시간복잡도로 구현이 될 것이다. 하지만, 덱을 활용하면 O(n)의 시간복잡도로 구할 수 있다.

  - 덱을 이용한 슬라이딩윈도우의 최댓값 구하기

    덱에 규칙을 부여하자. 덱의 앞쪽일수록 크기가 크고 오래된 수이다. 아래 예시를 통해 확인해보자.

    배열: `[9, 5, 3, 1, 6, 7]`, 윈도우 크기: `3`

    - `i=0` 데크가 비어 있으므로 인덱스 0추가, `[0]`
    - `i=1` 5는 현재 헤드의 9보다 작으므로 추가(나중에 9가 pop되면 최댓값이 될 수 있는 가능성이 존재함), `[0, 1]`
    - `i=2` 마찬가지로 3도 최댓값이 될 수 있는 가능성이 있으므로 추가, `[0, 1, 2]`
    - `i=3` 헤드가 윈도우 크기를 초과하므로 pop하고 1을 추가, `[1, 2, 3]`
    - `i=4` 뒤에서부터 6보다 작은수를 제거한다(오래된 수인데 현재수보다 작으면 최댓값이 될 수가 없음), `[4]`
    - `i=5` 마찬가지로 6을 제거하고 7을 추가한다, `[5]`

    -> 슬라이딩윈도우의 크기를 유지하기 위해 인덱스값을 사용한다. 그리고 각 해당 순서의 윈도우 내 최댓값은 덱의 헤드값이 최댓값이 된다.

    ```python
    import sys
    from collections import deque

    n, d = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))

    q = deque()
    dp = [-1] * n

    for i in range(n):
        # 최댓값을 유지하는 작업
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

        # 슬라이딩 윈도우 크기 유지
        while q and i - q[0] >= d:
            q.popleft()

        # dp 배열 업데이트
        dp[i] = lst[q[0]]

    print(dp)
    ```

  - 시간 복잡도 `O(n)`을 보장하는 이유

    - 각 요소는 데크에 최대 한 번 추가되고 한 번 제거된다.
    - 전체적으로 while문에 해당하는 연산은 2n을 넘지 않는다.
    - 따라서 시간복잡도 `O(n)`을 보장한다.

  - 연세워터파크 문제 해설

    ```python
    import sys
    sys.setrecursionlimit(10**6)

    n, d = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    dp = [float('inf')] * n

    def dfs(node):
        if dp[node] != float('inf'):
            return dp[node]

        result = lst[node]
        for i in range(1, d+1):
            next = node + i
            if next >= n:
                break

            result = max(result, lst[node] + dfs(next))
        dp[node] = result
        return dp[node]

    dfs(0)
    # print(dp)
    print(max(dp))
    ```

    위 코드처럼 dp로 문제를 쉽게 해결 가능하지만 결국 슬라이딩 윈도우 크기의 최댓값을 구하는 과정때문에 O(n x m)이라서 시간초과가 발생한다. 따라서 위 기법을 활용해서 현재 요소 전까지의 윈도우 내 최댓값과 현재 요소 값을 더한 값으로 최신화하면 O(n)시간복잡도로 정답을 구할 수 있다.

<br>
