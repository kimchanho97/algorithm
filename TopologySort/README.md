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
