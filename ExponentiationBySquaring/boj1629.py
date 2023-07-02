import sys

a, b, c = map(int, sys.stdin.readline().split())

def mul(a, b):
  if b == 1:
    return a % c
  if b % 2 == 0:
    return mul(a, b//2) ** 2 % c
  else:
    return a * (mul(a, (b-1)//2) ** 2) % c

print(mul(a, b))