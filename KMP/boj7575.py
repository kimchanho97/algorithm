# 3 4
# 13
# 10 8 23 93 21 42 52 22 13 1 2 3 4
# 11
# 1 3 8 9 21 42 52 22 13 41 42
# 10
# 9 21 42 52 13 22 52 42 12 21

import sys

n, k = map(int, sys.stdin.readline().split())
program = []
for _ in range(n):
    t = int(sys.stdin.readline())
    program.append(list(sys.stdin.readline().split()))

# print(program)

def kmp_table(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return

def kmp(text, pattern):
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]

        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                return True
    return False

result = False
for i in range(len(program[0]) - k + 1):
    pattern = program[0][i:i+k]
    table = [0] * len(pattern)
    kmp_table(pattern)
    # print(i, pattern)

    flag = True
    for j in range(1, n):
        text = program[j]
        if kmp(text, pattern):
            continue

        text = program[j][::-1]
        if kmp(text, pattern):
            continue

        flag = False
        break

    if flag:
        result = True
        # print(pattern)
        break

print("YES" if result else "NO")