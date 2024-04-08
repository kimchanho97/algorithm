## [골드3]레이저 통신(http://www.acmicpc.net/problem/6087)

- 문제: 'C'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오.(방향전환을 할 때마다 거울을 설치 -> 최소 방향전환)

  ```
  7 . . . . . . .         7 . . . . . . .
  6 . . . . . . C         6 . . . . . /-C
  5 . . . . . . *         5 . . . . . | *
  4 * * * * * . *         4 * * * * * | *
  3 . . . . * . .         3 . . . . * | .
  2 . . . . * . .         2 . . . . * | .
  1 . C . . * . .         1 . C . . * | .
  0 . . . . . . .         0 . \-------/ .
    0 1 2 3 4 5 6           0 1 2 3 4 5 6
  ```

* 알고리즘: `다익스트라`

* 해설: 방향전환 횟수를 우선순위로 두고 그래프 탐색을 수행한다.

  - 힌트

    - 방문처리(시간 초과 방지)

      만약 해당 방향으로 이미 방문한 적이 있는 경우, 방향 전환 횟수가 작다면 방문하고 같다면 생략한다.

      ```
      ..*
      *..
      ..*
      ```

      위와 같은 경우 (1, 3)을 가기 위해 위, 아래 동일한 방향의 경로가 중복된다. 이런 경우를 방지할 수 있음

    - 방향 전환 횟수가 작으면 무조건 힙에 추가하고, 같더라도 이전의 방향이 다를 경우 추가한다.

  - 입력

    ```
    7 8
    .......
    ......C
    ......*
    *****.*
    ....*..
    ....*..
    .C..*..
    .......
    ```

  - 출력

    ```
    3
    ```

<br>

## [골드2]미확인 도착지(http://www.acmicpc.net/problem/9370)

- 문제: 그래프와 시작점이 주어지고 각각의 후보 노드들이 주어질 때, 시작점에서 후보 노드로 가는 최단 경로가 특정 간선을 지나가는 경로인지 구하여라(특정 간선은 고정으로 주어진다.)

* 알고리즘: `다익스트라`

* 해설: g와 h 사이의 거리를 특정 간선이라고 친다면 후보 노드까지 최단 경로는 특정 간선을 포함하여야 한다.

  - 힌트: 2가지 경우의 수가 존재한다.

    - case1 = s -> (...) -> g -> h -> (...) -> node
    - case2 = s -> (...) -> h -> g -> (...) -> node

  - 위 경우의 최단 경로 거리값을 비교하여 만약 같다면 간선을 포함하는 것이다.

  - 입력

    ```
    2
    5 4 2
    1 2 3
    1 2 6
    2 3 2
    3 4 4
    3 5 3
    5
    4
    6 9 2
    2 3 1
    1 2 1
    1 3 3
    2 4 4
    2 5 5
    3 4 3
    3 6 2
    4 5 4
    4 6 3
    5 6 7
    5
    6
    ```

  - 출력

    ```
    4 5
    6
    ```

<br>