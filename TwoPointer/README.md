## [골드5]두 용액(http://www.acmicpc.net/problem/2470)

- 문제: 수열이 주어졌을 때, 두 수의 합이 0에 가장 가까운 수들의 조합을 찾아라.

* 알고리즘: `투 포인터`

* 해설

  ```
  10
  -10 -7 -5 -2 2 4 6 15 30 50

  -10 + 50 = 40
  -10 + 30 = 20
  -10 + 15 = 5
  -10 + 6 = -4
  -7 + 6 = -1
  -5 + 6 = 1
  -5 + 4 = -1
  -2 + 4 = 2
  -2 + 2 = 0
  ```

  ```python
  l, r = 0, n-1
  diff = abs(lst[l] + lst[r])
  left, right = lst[l], lst[r]
  while l < r:
      num = lst[l] + lst[r]
      print(f"{lst[l]} + {lst[r]} = {num}")
      if abs(num) < diff:
          diff = abs(num)
          left, right = lst[l], lst[r]

      if num < 0:
          l += 1
      elif num == 0:
          break
      else:
          r -= 1
  ```

  항상 합이 0에 가깝도록 수들을 조합해서 탐색을 진행한다.

  - 입력

    ```
    5
    -2 4 -99 -1 98
    ```

  - 출력

    ```
    -99 98
    ```

<br>

## [골드4]부분 합(http://www.acmicpc.net/problem/1806)

- 문제: 수열이 주어졌을 때, 연속된 수열의 부분합이 S이상인 수열 중 가장 짧은 부분 수열의 길이를 구하여라.

* 알고리즘: `투 포인터`

* 해설

  ```python
  l, r = 0, 0
  temp = 0
  answer = sys.maxsize
  # l부터 r-1 까지의 합
  while True:
      if temp < s:
          if r == n:
              break
          temp += lst[r]
          r += 1
      else:
          answer = min(r - l, answer)
          temp -= lst[l]
          l += 1
  ```

  부분합이 S보다 작을 경우, 길이를 증가시킨다. 부분합이 S보다 큰 경우, 길이를 감소시킨다. 중요한 점은 l부터 r-1까지의 부분합으로 만약 l과 r이 같은 경우, temp는 0이므로 r을 +1하고 temp를 더해준다.

  - 입력

    ```
    10 15
    5 1 3 5 10 7 4 9 2 8
    ```

  - 출력

    ```
    2
    ```

<br>
