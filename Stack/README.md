## [골드4]오큰수(http://www.acmicpc.net/problem/17298)

- 문제: 수열의 크기가 1,000,000일 때, Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 각 원소의 오큰수를 구하여라

* 알고리즘: `스택`

* 해설: 시간제한이 1초이기 때문에 한번의 반복문으로 답을 구해야한다.

  - 힌트: `9 8 7 6 5 4 3 2 1 10`수열의 오큰수를 구하면 모든 수가 10을 오큰수로 가진다. **값이 커질 때 오큰수를 결정하는 로직이 실행된다는 것**을 캐치해야 한다.

  - 입력

    ```
    4
    3 5 2 7
    ```

  - 출력

    ```
    5 7 7 -1
    ```

<br>