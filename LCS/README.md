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

## [골드5]공통 부분 문자열(http://www.acmicpc.net/problem/5582)

- 문제: LCS(Longest Common Substring, 가장 긴 공통 부분 문자열)문제
    - Longest Common Subsequence: 연속적일 필요 없이 두 문자열에서 순서를 유지하면서 일치하는 문자의 최대 길이를 구하는 문제
    - **Longest Common Substring**: 연속된 부분 문자열이 일치하는 경우에만 길이를 증가시키면서 문자열의 최대 길이를 구하는 문제

* 알고리즘: `DP`

* 해설

  각 문자열의 길이를 `N`과 `M`이라고 한다면 시간복잡도는 `O(N X M)`이다. `dp[i][j]`를 문자열`str1[:i]`과 문자열`str2[:j]`의 최장 공통 부분 문자열의 길이라고 정하자.

  만약 `i`와 `j`에서 같다면 공통 부분 문자열은 연속적이기 때문에 `str1[:i-1]`과 문자열`str2[:j-1]`의 최장 공통 부분 문자열의 길이인 `dp[i-1][j-1]`에 `+1`한 것과 같을
  것이다.

  ```python
  for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            result = max(result, dp[i][j])
  ```

  ```
  ADABREA
  EAADADABR

      E A A D A D A B R
    0 0 0 0 0 0 0 0 0 0
  A 0 0 1 1 0 1 0 1 0 0
  D 0 0 0 0 2 0 2 0 0 0
  A 0 0 1 1 0 3 0 3 0 0
  B 0 0 0 0 0 0 0 0 4 0
  R 0 0 0 0 0 0 0 0 0 5
  E 0 1 0 0 0 0 0 0 0 0
  A 0 0 2 1 0 1 0 1 0 0
  ```

    - Longest Common Subsequence: 연속적일 필요가 없으므로, 이전 값에서 최댓값만 유지하면 된다.
        - `dp[i][j] = max(dp[i][j-1], dp[i-1][j])`
    - **Longest Common Substring**: 연속적이어야 하므로, 일치하지 않을 경우 값이 `0`이다.
        - 그렇기 때문에 최댓값을 매번 갱신해야 한다.

- 문자열 알고리즘
    - kmp: 문자열 패턴 매칭 문제, `pattern`이 고정된 경우에만 사용 가능
    - trie: 공통 접두사(`prefix`)를 처리해야 하는 경우
    - 일반적으로 구현, `DP`

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
