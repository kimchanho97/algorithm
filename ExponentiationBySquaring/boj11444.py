import sys

n = int(sys.stdin.readline())
matrix = [[1, 1], [1, 0]]

def matrixMul(a, b):
  # 행렬 곱셈 
  c = [[0, 0], [0, 0]]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        c[i][j] += (a[i][k] * b[k][j])
      c[i][j] %= 1000000007
  return c

def fibo(n):
  if n == 1:
    return matrix
  if n % 2 == 1:
    temp = fibo((n-1)//2)
    return matrixMul(matrixMul(temp, temp), matrix)
  else:
    temp = fibo(n//2)
    return matrixMul(temp, temp)

result = fibo(n)
print(result[0][1])