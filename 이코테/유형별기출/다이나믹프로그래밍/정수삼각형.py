import sys
input = sys.stdin.readline

n = int(input())
pyramid = []
for _ in range(n):
    pyramid.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(pyramid[i])):
        if j == 0:
            pyramid[i][j] += pyramid[i-1][j]
        elif j == i:
            pyramid[i][j] += pyramid[i-1][j-1]
        else:
            pyramid[i][j] += max(pyramid[i-1][j-1], pyramid[i-1][j])

result = 0
for i in range(n):
    result = max(result, pyramid[n-1][i])

print(result)