## [골드4]파일 합치기3(http://www.acmicpc.net/problem/13975)

- 문제: 파일 크기가 배열로 주어지고, 파일을 합치는 비용은 파일 크기의 합이다. 이 파일들을 하나의 파일로 합칠 때 최소비용을 구하여라.

* 알고리즘: `우선순위 큐`, `그리디`

* 해설: 파일이 합쳐질 때 기존의 파일크기만큼 비용이 더해진다. 그러므로 파일 크기가 클수록 나중에 파일을 합치고 먼저 합치는 파일의 크기는 작아야 한다.

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
    826
    ```
