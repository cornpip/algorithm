import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

load = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    load[a].append(b)
    load[b].append(a)

dis = [INF] * (n+1)
q = []
dis[1] = 0
# 같은거는 아직 안들렸다는 뜻
# [현재까지 비용, 노드]
heapq.heappush(q, [0, 1])
while q:
    dist, now = heapq.heappop(q)
    if dis[now] < dist:
        continue
    for i in load[now]:
        cost = dist + 1
        if cost < dis[i]:
            dis[i] = cost
            heapq.heappush(q, [cost, i])

count = 0
min_index = 0
for i in range(n, 0, -1):
    if dis[i] == dis[n]:
        count += 1
        min_index = i

print(min_index, dis[n], count)