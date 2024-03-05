## [골드1]부분수열의 합(http://www.acmicpc.net/problem/1208)

- 문제: 수열이 주어지고 크기가 양수인 부분수열의 합이 S가 되는 경우의 수를 구하는 문제
  - 조건: 수열의 길이 (1 <= N <= 40)
  - 함정: 단순히 완전탐색으로 해결하면 각 원소가 (포함 or 포함x) 2개의 경우의 수를 가진다. -> 시간복잡도: 2^N(40)

* 알고리즘: `Meet in the middle`

* 해설: 완전 탐색으로 구할 경우 2^40으로 시간초과가 발생한다. `Meet in the middle` 알고리즘을 통해 배열을 left, right로 나눈 뒤 두 부분 수열의 합이 S가 되는 경우의 수를 구한다. 시간복잡도: 2^20(=1024 \* 1024)
  위 경우는 left, right의 원소를 모두 가지는 부분수열로 추가적으로 left만으로 가능한 조합, right만으로 가능한 조합을 더해주어야 한다.

  - 입력

    ```
    5 0
    -7 -3 -2 5 8
    ```

  - 출력

    ```
    1
    ```

* 참고: 부분수열의 합을 구하는 코드

  ```python
    def get_sum(arr):
        sum_arr = [0]
        for num in arr:
            new_sum_arr = []
            for i in sum_arr:
                new_sum_arr.append(i + num)
            sum_arr.extend(new_sum_arr)

        sum_arr.remove(0) # 아무것도 포함하지 않는 경우
        sum_arr.sort()
    return sum_arr
  ```

<br>
