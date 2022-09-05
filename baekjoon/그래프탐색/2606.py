import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [ False ] * (n+1)
def bfs():
    q = deque()
    q.append(1)
    count = -1
    while q:
        now = q.popleft()
        if visited[now] == True:
            continue
        visited[now] = True
        count += 1;
        for i in graph[now]:
            q.append(i)
    return count

print(bfs())