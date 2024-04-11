# ABC ABCDAB ABCDABCDABDE
# ABCDABD

def kmp_table():
    j = 0  # j = 접두사 인덱스
    for i in range(1, len(pattern)):  # i = 접미사 인덱스
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return

def kmp():
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]

        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                result.append(i - j + 2)
                j = table[j - 1]
    return

import sys

text = sys.stdin.readline().strip('\n')
pattern = sys.stdin.readline().strip('\n')
table = [0] * len(pattern)
result = []

kmp_table()
kmp()
# print(table)
print(len(result))
print(*result)