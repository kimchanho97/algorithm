import sys

class Node:
    def __init__(self, key, data=None) -> None:
        # key = char, data = string(leaf node에 저장)
        self.key = key
        self.data = data
        self.child = dict()

class Trie:
    def __init__(self) -> None:
        self.head = Node(None)
    
    # 문자열 추가: 리턴값 없음
    def insert(self, string) -> None:
        curNode = self.head
        for char in string:
            # 문자가 없을 경우 -> 추가한 후 이동
            if char not in curNode.child:
                curNode.child[char] = Node(char)
            # 문자가 있을 경우 -> 이동
            curNode = curNode.child[char]
        
        # 끝나는 Node에 문자열 data 추가
        curNode.data = string

    # Prefix 존재 여부 검사: True or False
    # 모든 문자열은 Trie에 추가된 상태
    def isPrefix(self, string):
        curNode = self.head
        # 문자열의 끝 Node로 이동
        for char in string:
            curNode = curNode.child[char] 
        # 자식이 있는 경우(leaf가 아님)
        if curNode.child:
            return True
        return False

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    # Trie 초기화
    trie = Trie()
    strings = []
    for i in range(n):
        inputString = sys.stdin.readline().rstrip()
        strings.append(inputString)
        trie.insert(inputString)
    
    is_True = True
    for string in strings:
        if trie.isPrefix(string):
            is_True = False
    
    print('YES' if is_True else 'NO')