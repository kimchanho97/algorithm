import sys

n, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int ,sys.stdin.readline().split(' '))) for _ in range(n)]
for i in range(n):
  for j in range(n):
    matrix[i][j] %= 1000

def matrixMul(a, b):
  # 행렬 곱셈함수
  c = [[0] * len(a) for _ in range(len(a))]
  for i in range(len(a)):
    for j in range(len(a)):
      for k in range(len(a)):
        c[i][j] += (a[i][k] * b[k][j])
      c[i][j] %= 1000
  return c

def power(matrix, n):
  # matrix를 n 제곱한 결과
  if n == 1:
    return matrix
  if n % 2 == 1:
    temp = power(matrix, (n-1)//2)
    return matrixMul(matrixMul(temp, temp), matrix)
  else:
    temp = power(matrix, n//2)
    return matrixMul(temp, temp)

result = power(matrix, b)
for i in range(n):
  for j in range(n):
    print(result[i][j], end=' ')
  print()