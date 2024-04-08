# 8
# A
# AS
# AST
# ASTV
# ASB
# AV
# AVC
# AC

import math
import sys

sys.setrecursionlimit(10**4)

class Node:
    def __init__(self, key):
        self.key = key
        self.data = None
        self.child = dict()

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.child:
                cur_node.child[char] = Node(char)
            cur_node = cur_node.child[char]
        cur_node.data = 1
        return

def longest_common_prefix(ori, ano):
    # original(대상), another(비교군)
    idx = 0
    for i in range(len(ori)):
        idx = i
        if i == len(ano) or ori[i] != ano[i]:
            break

    return ori[:idx + 1]

def dfs(node):
    cnt = 1
    if not node.child:
        return cnt

    if node.data:
        cnt = math.factorial(len(node.child)) * (len(node.child) + 1)
    else:
        cnt = math.factorial(len(node.child))

    for next_node in node.child:
        cnt *= dfs(node.child[next_node])

    return cnt % 1_000_000_007

trie = Trie()
n = int(sys.stdin.readline())
lst = [sys.stdin.readline().rstrip() for _ in range(n)]
lst.sort()
# print(lst)

for i in range(n):
    if i == 0:
        string = longest_common_prefix(lst[i], lst[i+1])
    elif i == n - 1:
        string = longest_common_prefix(lst[i], lst[i-1])
    else:
        left = longest_common_prefix(lst[i], lst[i - 1])
        right = longest_common_prefix(lst[i], lst[i + 1])
        # 긴 string을 insert
        if len(right) > len(left):
            string = right
        else:
            string = left
    # print(i, lst[i], string)
    trie.insert(string)

# print(trie.head)
# print(trie.head.child)

print(dfs(trie.head))