## [골드4]스도쿠(http://www.acmicpc.net/problem/2239)

- 문제: 전형적인 백트래킹 문제

  가능한 수의 조합을 모두 탐색해서 스도쿠를 만족할 경우 프로그램을 종료

* 알고리즘: `백트래킹`

* 해설

  ```python
  def BT(idx):
    if idx == len(blank):
        for line in board:
            print(''.join(map(str, line)))
        sys.exit(0)

    row, col = blank[idx]
    for num in range(1, 10):
        if not is_exist_row(row, num) and not is_exist_col(col, num) and not is_exist_square(row, col, num):
            board[row][col] = num
            BT(idx + 1)
            board[row][col] = 0

    return
  ```

  중요한 점: 해당 경로가 틀린 길일 경우 다시 원상태로 돌려놓는 코드가 존재해야지 다음 경로에 영향을 안준다. `board[row][col] = 0`

  - 입력

    ```
    103000509
    002109400
    000704000
    300502006
    060000050
    700803004
    000401000
    009205800
    804000107
    ```

  - 출력

    ```
    143628579
    572139468
    986754231
    391542786
    468917352
    725863914
    237481695
    619275843
    854396127
    ```

<br>
