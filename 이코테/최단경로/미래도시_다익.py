import heapq
import sys
sys.path.append("C:/Users/choi/VscodeProject/Algorithm/이코테/Package")
import simplytime as time

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

def dijkstra(start):
    q =[]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

time.s()
dijkstra(1)
toX = distance[k]

distance = [INF] * (n+1)
dijkstra(k)
toK = distance[x]

if toX + toK >= INF:
    print(-1)
else:
    print(toX + toK)
time.f()