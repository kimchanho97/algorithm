import sys
from itertools import combinations

def wordToBit(word):
    bit = 0
    for i in word:
        bit = bit | (1 << (ord(i) - ord('a')))
    return bit
    # return bin(bit)

n, k = map(int, sys.stdin.readline().split())
words = [wordToBit(sys.stdin.readline().strip()) for _ in range(n)]
if k < 5:
    print(0)
    sys.exit()

baseBit = wordToBit('actin')
result = 0
for alphas in combinations('bdefghjklmopqrsuvwxyz', k-5):
    comb = wordToBit(''.join(alphas))
    comb |= baseBit
    count = 0
    for word in words:
        if word & comb == word:
            count += 1
    result = max(result, count)
    
print(result)