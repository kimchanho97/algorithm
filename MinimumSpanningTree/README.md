## [골드4]최소 스패닝 트리(http://www.acmicpc.net/problem/1197)

- 문제: 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 문제

* 알고리즘: `크루스칼 알고리즘`, `유니온 파인드`

* 해설

  - 크루스칼 알고리즘
    간선들을 cost값순으로 오름차순 정렬한 이후, 시작점과 끝점의 연결 여부를 유니온파인드로 알아낸 뒤, 연결되어 있으면 pass하고, 각각의 루트가 다를 경우 머지해서 연결시키고 cost를 더해준다.

  - 입력

    ```
    3 3
    1 2 1
    2 3 2
    1 3 3
    ```

  - 출력

    ```
    3
    ```

<br>

## [골드3]우주신과의 교감(http://www.acmicpc.net/problem/1774)

- 문제: 각 점들의 좌표가 주어졌을 때, 모든 좌표를 하나로 연결하는 최소 비용을 구해라.

* 알고리즘: `크루스칼 알고리즘`, `유니온 파인드`

- 유니온파인드

  ```python
  def find(n):
    if p[n] < 0:
        return n
    else:
        p[n] = find(p[n])
        return p[n]

  def merge(a, b):
      root_a = find(a)
      root_b = find(b)
      if root_a != root_b:
          p[root_a] += p[root_b]
          p[root_b] = root_a
          return True
      return False
  ```

  - find: 경로를 찾는 과정에서 바로 부모 노드로 연결
  - merge: 루트를 비교하는 로직을 함수 내 포함시켜 중복 로직을 최소화하고 merge가 이뤄진 경우 True를 리턴한다.

* 함정:

  - 이미 연결된 좌표의 입력이 오름차순이 아닐 수 있음 -> 반대 상황까지 고려
  - 이미 연결된 좌표의 입력이 이미 연결을 형성중 일 수 있음 -> 만약 연결되지 않은 경우, merge
  - 이미 연결된 좌표들이 mst가 아닌 사이클을 형성할 수도 있음 -> 큐를 모두다 반복순회

* 해설

  - 입력

    ```
    4 1
    1 1
    3 1
    2 3
    4 3
    1 4
    ```

  - 출력

    ```
    4.00
    ```

<br>