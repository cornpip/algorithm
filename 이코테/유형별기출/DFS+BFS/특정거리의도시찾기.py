from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
q = deque()

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, f = map(int, input().split())
    graph[s].append(f)

result = []
visited = [[False] for _ in range(n+1)]
q.append((x, 0))
while q:
    now, dist = q.popleft()
    if visited[now] == True:
        continue
    if dist == k:
        result.append(now)
    if dist == k+1:
        break
    visited[now] = True
    for node in graph[now]:
        q.append((node, dist+1))

if not result:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)