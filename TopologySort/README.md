## [골드3]음악프로그램(http://www.acmicpc.net/problem/2623)

- 문제: 가수의 출연 순서가 각각 주어졌을 떄, 전체 가수의 순서를 정하는 프로그램을 작성하시오.

* 알고리즘: `위상 정렬`

* 해설

  - 위상 정렬

    그래프가 방향이 존재하는 유향그래프일 때, 각 노드의 방문 순서를 정렬하는 것이다. **위상 정렬이 필요한 경우는 그래프에서 반드시 자신보다 선행되어야 할 일을 다 끝내야만 작업에 들어갈 수 있는(방문할 수 있는) 조건이 주어질 때**이다.

    <img width="450" alt="스크린샷 2024-07-04 오후 7 51 19" src="https://github.com/kimchanho97/algorithm/assets/104095041/53f35ba4-1887-469e-86ce-643f1cabe3ee">

  - 위상 정렬이 불가능한 경우

    <img width="450" alt="스크린샷 2024-07-04 오후 7 51 33" src="https://github.com/kimchanho97/algorithm/assets/104095041/2a8fb1d8-1b53-42bc-8596-03e906b9d0e2">

    **사이클이 존재하는 경우**: 위상 정렬은 각각의 노드를 한 번씩 방문해서 총 V(vertex)개수 만큼 방문한다. 하지만 사이클이 존재하는 경우 V번 방문을 하기 전에 for문이 종료된다.

  - 전처리

    ```python
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(m):
        seq = list(map(int, sys.stdin.readline().split()))[1:]
        for i in range(len(seq) - 1):
            s = seq[i]
            e = seq[i + 1]
            graph[s].append(e)
            indegree[e] += 1
    ```

  - 정렬 알고리즘

    ```python
    def topology_sort(indegree, graph):
        q = deque()
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)

        result = []
        for i in range(n):
            if not q:
                return [0]

            cur = q.popleft()
            result.append(cur)
            for next in graph[cur]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)
        return result
    ```

    노드 개수만큼만 반복을 수행하며 for문 도중 **큐의 크기가 2이상이라면 가능한 위상 정렬의 결과가 2개 이상이라는 의미**이다.

  - 입력

    ```
    6 3
    3 1 4 3
    4 6 2 5 4
    2 2 3
    ```

  - 출력

    ```
    6
    2
    1
    5
    4
    3
    ```

<br>

## [플래5] 임계경로 (http://www.acmicpc.net/problem/1948)

- 문제: 비순환 방향 그래프(DAG)가 주어졌을 때, 출발지점부터 도착지점까지 최대 비용을 구하고, 해당 경로의 간선 개수를 구하여라.

- 알고리즘: `위상 정렬`, `경로 추적`

- 해설

  <img src="https://github.com/user-attachments/assets/4bef6971-6fc6-4d79-be9a-2328c2f16d76" width=800>

  - 문제를 푸는 방법: 출발지점으로부터 도착지점까지의 각각의 경로를 탐색하고 최대 비용을 구한 뒤, 그 경로를 역추적하여 간선의 개수를 구합니다.
  - 처음에는 최대 비용을 구하기 위해 각각의 경로를 DFS, BFS로 구현했으나, DFS와 BFS 모두 중복 경로 탐색 문제가 발생했습니다.

- 예시: 경로 중복 문제

  - 만약, 경로 path 1, 2, 3, 4가 존재하고 이 경로들이 노드 6에서 만난 이후 동일한 경로를 따른다고 가정합시다.
  - DFS를 사용할 경우, 노드 6에 도달하기까지 비용이 각각 5, 6, 7, 8이라면, 노드 6 이후의 경로를 4번 반복해서 탐색하게 됩니다. 즉, 경로가 중복되면서 불필요한 탐색이 발생하게 되는 것이죠.
  - BFS도 마찬가지로 path 1, 2, 3, 4를 큐에 모두 추가하며 중복된 경로를 탐색합니다.

- 조건 추가한 BFS/DFS도 한계 존재

  - 이러한 문제를 해결하기 위해, 경로 비용이 더 큰 경우에만 탐색을 진행하도록 조건을 추가하여 `if`문으로 필터링했지만, 여전히 **중복 탐색**이 발생했습니다.
  - 이유는 노드 6에 도달한 후 **이전 경로들이 완전히 처리되지 않았기 때문**입니다. 즉, **모든 경로를 고려하지 않고** 경로 비용이 갱신될 때마다 다시 탐색이 이루어지기 때문에 중복이 발생합니다.

- 해결책: 위상 정렬을 통한 중복 제거

  - **위상 정렬**은 노드 6에 도달하는 **이전 경로들이 모두 처리된 후**에만 탐색이 이루어지므로, 경로가 중복되지 않으며 불필요한 탐색을 줄입니다.
  - 위상 정렬은 DAG에서 노드를 **순차적으로 처리**하면서 최적 경로를 구하므로, 중복 경로 처리 문제를 해결할 수 있습니다.

- **코드 예시**:
  ```python
  def topology_sort(node):
      q = deque([node])
      while q:
          curNode = q.popleft()
          count[curNode] += 1
          for nextNode, cost in graph[curNode]:
              dp[nextNode] = max(dp[nextNode], dp[curNode] + cost)
              indegree[nextNode] -= 1
              if indegree[nextNode] == 0:
                  q.append(nextNode)
  ```
  ```python
  def bfs(node):
      q = deque([(node, 0)])
      while q:
          curNode, curSum = q.popleft()
          count[curNode] += 1
          for nextNode, cost in graph[curNode]:
              if dp[nextNode] > curSum + cost:
                  continue
              q.append((nextNode, curSum + cost))
              dp[nextNode] = curSum + cost
  ```
  ```python
  def dfs(node, sum):
      dp[node] = max(dp[node], sum)
      count[node] += 1
      for nextNode, cost in graph[node]:
          if sum + cost > dp[nextNode]:
              dfs(nextNode, sum + cost)
  ```
- **결과 비교**:

  ```less
  위상정렬: [0, 1, 1, 1, 1, 1, 1, 1]
  bfs: [0, 1, 1, 1, 1, 1, 2, 3]
  dfs: [0, 1, 1, 1, 1, 1, 2, 2]
  ```

- **count 배열**을 선언하여 각 탐색 방법이 노드를 얼마나 방문했는지 확인해보면, 위상 정렬은 **한 번의 방문만**을 보장합니다. 반면, BFS와 DFS는 경로가 중복될 때마다 여러 번 방문하는 것을 확인할 수 있습니다.
- 위상 정렬은 `indegree == 0`인 노드만 추가되므로, 각 노드가 한 번만 처리됨을 보장한다.
- 따라서, 비순환 방향 그래프(DAG)에서는 **한 번의 방문이 아닌 경로 비용을 기준으로 중복 방문을 허용**하는 경우, **가장 빠른 탐색 방법**은 **위상 정렬**입니다.
