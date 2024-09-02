## [골드4]공유기 설치(http://www.acmicpc.net/problem/2110)

- 문제: 집의 좌표를 나타내는 `xi (0 ≤ xi ≤ 1,000,000,000)`가 한 줄에 하나씩 주어진다. 집의 개수 `N (2 ≤ N ≤ 200,000)`와 공유기의 개수 `C (2 ≤ C ≤ N)`가 주어졌을 때, 가장 인접한 두 공유기 사이의 최대거리를 구하여라.

  **요약: n개의 좌표 배열에서 r개를 선택한 nCr조합 중 각각의 좌표간의 거리의 최솟값이 가장 큰 경우를 찾는 문제**

  ```
  (1, 4, 7, 10, 13) -> 3
  (1, 3, 7, 10, 10) -> 2
  (1, 2, 4, 9) -> 1
  ```

* 알고리즘: `이분탐색`

* 해설

  - 완전탐색인 경우, 각각의 combination의 최솟값을 최대로 하는 방식으로 구할 수 있지만, `nCr`에서 시간초과가 발생한다. 따라서 새로운 접근법이 필요
  - 두 공유기 사이의 거리는 최소가 `1`, 최대가 양 끝 집 사이의 거리이다. mid값을 두 인접한 공유기 사이의 거리 중 최솟값이라고 생각하고 이분탐색을 실시한다.

  ```python
  minL = 1
  maxL = (lst[n-1] - lst[0]) // (m-1)
  result = 1
  while minL <= maxL:
      curL = (minL + maxL) // 2
      prevP = lst[0]
      cnt = 1
      for i in range(1, n):
          curP = lst[i]
          dist = curP - prevP
          if dist >= curL:
              cnt += 1
              prevP = curP

      if cnt >= m:
          result = max(result, curL)
          minL = curL + 1
      else:
          maxL = curL - 1
  ```

  -> mid값을 기준으로 설치 가능한 곳에 공유기를 설치한다. 만약 설치한 개수가 기존의 공유기 개수를 넘을 경우, 이는 가능한 경우의 수이므로 최댓값을 최신화한다.

<br>
