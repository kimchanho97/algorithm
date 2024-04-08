## 모든 경로 탐색

- 문제: 그래프가 주어졌을 때, (1, 1)에서 (N, N)으로 가는 경로 중 방향 전환 횟수가 k인 경로가 존재하는지 구해라. (1, 1)에서의 방향은 사용자가 정할 수 있다.

* 알고리즘: `DFS`, `백트래킹`

* 해설

  - 방향 전환 횟수가 최소 또는 최대가 아닌 특정 k이기 때문에 완전탐색으로 모든 경로의 방향 전환 횟수를 구한 뒤 k와 비교해서 존재하는지 파악한다.

  - 모든 경로를 탐색하기 위해서는 DFS를 통해서 각각의 path를 독립적으로 탐색한다. 또한 백트래킹 기법을 통해 방문 처리를 동적으로 처리해줌으로써 경로 탐색이 종료될 때, 다시 미방문 처리로 바꾸어 준다.

    ```python
    def dfs(r, c, dir, cnt, path):
    # 방문 처리 & 경로 추가
    visit[r][c] = True
    path.append((r, c))
    if (r, c) == (n-1, n-1):
        result.append([cnt, path[:]])

    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(4):
        dr, dc = move[i][0], move[i][1]
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 0:
            if not visit[nr][nc]:
                if i == dir:  # 같은 방향
                    dfs(nr, nc, i, cnt, path)
                else:  # 다른 방향(회전)
                    dfs(nr, nc, i, cnt + 1, path)

    visit[r][c] = False
    path.pop()
    return
    ```

  - 입력

    ```
    3
    2 2
    0 1
    0 0
    2 3
    0 1
    0 0
    3 3
    0 1 0
    0 0 1
    0 0 0
    ```

  - 출력

    ```
    True
    False
    True
    ```

<br>
