## [골드3]세 용액(http://www.acmicpc.net/problem/2473)

- 문제: 수열이 주어졌을 때, 세 수의 합이 0에 가장 가까운 수들의 조합을 찾아라.

* 알고리즘: `투 포인터` or `이분 탐색`

* 해설

  참고: [골드5]두 용액(http://www.acmicpc.net/problem/2470)

  - 투 포인터

    세 수의 합이 0이 되려면 위 문제(두 용액)을 참고해서 두 수의 합이 나머지 수의 음수와 같으면 된다. 기준이 되는 수를 for문으로 반복한 뒤, 반복문 안에서 투포인터 로직을 실행한다.

    ```python
    for i in range(n):
    l, r = i+1, n-1
    center = lst[i]
    while l < r:
        # 두개의 합이 -center가 되어야 함
        curSum = lst[l] + lst[r]
        if abs(curSum + center) < result:
            result = abs(curSum + center)
            answer = [i, l, r]

        if curSum < -center:
            l += 1
        elif curSum == -center:
            break
        else:
            r -= 1
    ```

    l을 i+1로 지정해도 되는 이유는 결국 중첩 반복문을 실행할 때 중복을 제거하려면 내부 반복문의 인덱스가 바깥 반복문의 인덱스보다 커야된다. 만약 `i=2`일 때, `l=0`, `r=5`로 갱신되었다고 하면 이미 `i=0`일 때 갱신되었을 것이다.

  - 이분 탑색

    이중 for문으로 가능한 모든 경우의 수를 구한 뒤 나머지 한 수의 합을 이분탐색으로 구하는 방법
    O(n^2 logN)으로 위 투포인터 O(n^2)보다 오래 걸리지만 통과한다.

<br>

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
