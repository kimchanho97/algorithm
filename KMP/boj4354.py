def kmp_table(pattern, table):
    # 최대의 접두사 접미사의 길이
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return

import sys

while True:
    s = sys.stdin.readline().strip()
    n = len(s)
    if s == ".":
        exit()
    table = [0] * len(s)

    kmp_table(s, table)
    # print(table)

    prefix = n - table[n - 1]
    # print(prefix)
    if n % prefix == 0:
        print(n // prefix)
        continue

    print(1)