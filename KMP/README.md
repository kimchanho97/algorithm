## [플래5]찾기(http://www.acmicpc.net/problem/1786)

- 문제: 문자열 매칭(KMP 알고리즘 구현)

- 알고리즘: `KMP`

- 해설

  아주 긴 문자열 TEXT에서 찾고자 하는 문자열 PATTERN을 찾는 알고리즘은 이중for문을 통해서 시간복잡도 O(NM)으로 구현이 가능하다.

  하지만, 이중 for문 내부의 pattern을 비교하는 과정(M의 과정)이 클수록 시간복잡도가 증가한다. KMP알고리즘은 시간복잡도 O(N + M)으로 이 문제를 해결한다.

  - 원리: **Pattern을 비교하는 과정에서 만약 실패하는 경우, 이전의 일치하는 정보를 재사용하는 것**

    <img width="700" alt="스크린샷 2024-04-11 오후 9 01 13" src="https://github.com/kimchanho97/algorithm/assets/104095041/f961dfe5-c8e0-4f57-9229-8a3a77824530">

    현재 Text의 접미사가 Pattern의 접두사와 일치를 보장한 곳은 굳이 다시 확인할 필요가 없다.

  - kmp_table

    값 = **접두사, 접미사가 같아지는 최대길이**

    <img width="450" alt="스크린샷 2024-04-11 오후 9 09 48" src="https://github.com/kimchanho97/algorithm/assets/104095041/64abcad2-cdda-4fe4-b56a-ac24e66398e2">

    kmp테이블을 구하는 과정에서도 kmp알고리즘을 활용한다.(패턴의 접미사 인덱스를 1부터 시작해서 비교한다.)

    ```python
    def kmp_table():
    j = 0  # j = 접두사 인덱스
    for i in range(1, len(pattern)):  # i = 접미사 인덱스
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return
    ```

  - kmp알고리즘

    ```python
    def kmp():
    j = 0  # j = 패턴의 접두사
    for i in range(len(text)):  # i = 텍스트의 접미사
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]

        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                result.append(i - j + 2)
                j = table[j - 1]
    return
    ```

  - 입력

    ```
    ABC ABCDAB ABCDABCDABDE
    ABCDABD
    ```

  - 출력

    ```
    1
    16
    ```

<br>
