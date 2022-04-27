import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = int(input()),int(input())

result = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    if c < result[a][b]:
        result[a][b] = c

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            result[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            result[i][j] = min(result[i][j], result[i][k]+result[k][j])

for i in range(1,n+1):
    for j in range(1, n+1):
        if result[i][j] == INF:
            print(0, end=" ")
        else:
            print(result[i][j],end=" ")
    print()