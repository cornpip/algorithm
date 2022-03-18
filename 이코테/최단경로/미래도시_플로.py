import sys
sys.path.append("C:/Users/choi/VscodeProject/Algorithm/이코테/Package")
import simplytime as time

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

time.s()
for k in range (1, n+1):
    for a in range (1, n+1):
        for b in range (1, n+1):
            if a==b:
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)
    
time.f()