import sys

class Node:
    def __init__(self, key, data=None) -> None:
        # key = 문자, data = 문자열
        self.key = key
        self.data = data
        self.child = dict()
        
class Trie:
    def __init__(self) -> None:
        self.head = Node(None)
    
    def insert(self, string) -> None:
        curNode = self.head
        for char in string:
            # 문자가 없을 경우
            if char not in curNode.child:
                curNode.child[char] = Node(char)
            curNode = curNode.child[char]
        curNode.data = string

    def checkCnt(self, string) -> int:
        cnt = 0
        curNode = self.head
        for char in string:
            # 시작 입력일 경우
            if curNode == self.head:
                cnt += 1
            # 선택지가 2개 이상일 경우
            elif len(curNode.child) > 1:
                cnt += 1
            # 종료 문자열이 있을 경우
            elif curNode.data != None:
                cnt += 1
            
            curNode = curNode.child[char]

        return cnt

while True:
    input = sys.stdin.readline().rstrip()
    if not input:
        break
    n = int(input)
    trie = Trie()
    words = []
    for i in range(n):
        string = sys.stdin.readline().rstrip()
        words.append(string)
        trie.insert(string)

    total = 0
    for i in words:
        total += trie.checkCnt(i)
    print(f'{total / len(words):.2f}')