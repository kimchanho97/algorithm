## [골드3]파일 합치기(http://www.acmicpc.net/problem/11066)

- 문제: 파일 크기가 배열로 주어지고, 파일을 합치는 비용은 파일 크기의 합이다. 이 파일들을 하나의 파일로 합칠 때 최소비용을 구하여라. 단, 연속된 파일만 합칠 수 있다.

* 알고리즘: `DP`

* 해설: `dp[i][j]`는 i부터 j까지의 최소비용으로 `dp[i][j] = min([(dp[i][k] + dp[k + 1][j])
for k in range(i, j)]) + (psum[j] - psum[i - 1])` 의 점화식을 가진다.
  결국 파일을 합칠 때는 2개의 파일(합쳐진 파일 or 하나의 파일)을 합치는 경우이다.
  - 입력
  ```
  4
  40 30 30 50
  15
  1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
  ```
  - 출력
  ```
  300
  864
  ```

<br>

## [골드3]내리막 길(http://www.acmicpc.net/problem/1520)

- 문제: 각 칸의 지점의 높이가 쓰여진 지도가 주어지고 항상 높이가 낮은 지점으로만 이동하여 목표지점까지 도달하고자 한다.

* 알고리즘: `DP`, `DFS`

* 해설: m, n의 크기가 500이하일 때, 방문처리를 안할 경우 그래프 탐색의 시간복잡도는 O(이동경로의 수 ^ (NM))이다. 예를 들어, m, n이 각각 2, 1일 경우 그래프의 크기가 2이므로 (상하좌우) x (상하좌우) = 4^2 의 경우의 수가 발생한다. 그러므로 O(4 ^ 500 x 500)의 시간복잡도를 가지므로 dp를 사용해서 이전에 이미 계산된 경로의 경우 반복된 계산을 하지 않도록 한다.
  - **목표지점에 도달했을 때 지나온 경로에 dp를 기록하는 것이 핵심이다.**
  - 입력
  ```
  4 5
  50 45 37 32 30
  35 50 40 20 25
  30 30 25 17 28
  27 24 22 15 10
  ```
  - 출력
  ```
  3
  ```

<br>

## [골드3]양팔저울(http://www.acmicpc.net/problem/2629)

- 문제: 추의 무게들이 오름차순으로 주어질 때, 양팔저울을 사용해서 미지의 구슬의 무게를 알 수 있는지 판단해라.

* 알고리즘: `DP`, `냅색 알고리즘`

* 해설: 주어진 추 무게 배열을 냅색 알고리즘을 통해서 이전에 계산한 무게들과 현재 추의 무게의 관계를 통해 구할 수 있는 무게를 최신화한다.
  - 경우의 수
    - 현재 추의 무게 - 이전 배열의 무게
    - 현재 추의 무게 + 이전 배열의 무게
    - **이전 배열의 무게 - 현재 추의 무게** -> 놓치기 쉬움
  - 입력
  ```
  2
  1 4
  2
  3 2
  ```
  - 출력
  ```
  Y N
  ```

<br>

## [골드3]앱(http://www.acmicpc.net/problem/7579)

- 문제: 필요한 메모리 M 바이트를 확보하기 위한 앱 비활성화의 최소의 비용을 계산

* 알고리즘: `DP`, `냅색 알고리즘`

* 해설:
  - 1 ≤ N ≤ 100, 1 ≤ M ≤ 10,000,000이며, 1 ≤ m1, ..., mN ≤ 10,000,000을 만족한다. 또한, 0 ≤ c1, ..., cN ≤ 100이고, M ≤ m1 + m2 + ... + mN을 만족한다.
  - **발상의 전환: M을 기준으로 냅색을 수행하면 배열의 크기가 너무 커진다. 그래서 인덱스를 비용으로 놓고 냅색을 수행**한다. 비용이 idx일때, 확보할 수 있는 최대 바이트를 `dp[i][j]`로 정의하고 냅색을 진행하면 된다.
  - 입력
  ```
  5 60
  30 10 20 35 40
  3 0 3 5 4
  ```
  - 출력
  ```
  6
  ```