# 에라토스테네스의 체
# 약수의 대칭성
import math

n = int(input())
arr = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n) + 1)):
    if arr[i] == True:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j += 1

for i in range(2, n+1):
    if arr[i]:
        print(i, end=" ")