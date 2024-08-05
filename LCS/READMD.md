## [골드5]LCS(http://www.acmicpc.net/problem/9251)

- 문제: LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제, 두 문자열의 LCS의 길이를 출력하라.

* 알고리즘: `DP`

* 해설

  각 문자열의 길이를 `N`과 `M`이라고 한다면 시간복잡도는 `O(N X M)`이다. `dp[i][j]`를 문자열`str1[:i]`과 문자열`str2[:j]`의 최장 공통 부분 수열의 길이라고 정하자.

  만약 `i`와 `j`에서 같다면 각 문자열의 길이에서 `-1`한 만큼의 문자열들의 최장 공통 부분 수열의 길이에 `+1`한 것과 같을 것이다.

  ```python
  dp = [[0] * (m+1) for _ in range(n+1)]
  # dp[i][j] : short[:i]와 long[:j]의 최대 공통 부분 수열의 길이
  for i in range(1, n+1):
      for j in range(1, m+1):
          if short[i-1] == long[j-1]:
              dp[i][j] = dp[i-1][j-1] + 1
          else:
              dp[i][j] = max(dp[i][j-1], dp[i-1][j])
  ```

  ```
  ACAYKP
  CAPCAKPP

      C A P C A K P P
    0 0 0 0 0 0 0 0 0
  A 0 0 1 1 1 1 1 1 1
  C 0 1 1 1 2 2 2 2 2
  A 0 1 2 2 2 3 3 3 3
  Y 0 1 2 2 2 3 3 3 3
  K 0 1 2 2 2 3 4 4 4
  P 0 1 2 3 3 3 4 5 5
  ```

<br>

## [골드4]LCS2(http://www.acmicpc.net/problem/9252)

- 문제: LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제, 두 문자열의 LCS의 길이와 문자열을 출력하라.

* 알고리즘: `DP`

- 참고: **[골드5]LCS(http://www.acmicpc.net/problem/9251)**

* 해설

  `dp`배열을 역으로 trace해서 해당 LCS문자열을 구한다. 현재 `dp[i][j]`값이 `dp[i-1][j-1]`과 차이가 난다면 해당 문자는 LCS문자열에 포함된다.

  ```python
  r, c = n, m
  answer = []
  while r > 0 and c > 0:
      # print(r, c)
      cur = dp[r][c]
      left = dp[r][c-1]
      up = dp[r-1][c]
      line = dp[r-1][c-1]
      if cur-1 == line and line == left and left == up:
          answer.append(long[c-1])
          r, c = r-1, c-1
          continue
      if cur == left:
          r, c = r, c-1
      else:
          r, c = r-1, c
  ```

<br>
