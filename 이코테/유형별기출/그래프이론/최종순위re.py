import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    pre = list(map(int, input().split()))

    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            graph[pre[i]][pre[j]] = True
            indegree[pre[j]] += 1
        
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            indegree[b] -= 1
            graph[b][a] = True
            indegree[a] += 1
        elif graph[b][a]:
            graph[b][a] = False
            indegree[a] -= 1
            graph[a][b] = True
            indegree[b] += 1

    q = deque()
    for i in range(1, (n+1)):
        if indegree[i] == 0:
            q.append(i)

    result = []
    donknow = False
    while q:
        if len(q) > 1:
            donknow = True
        team = q.popleft()
        result.append(team)
        for i in range(1,n+1):
            if graph[team][i]:
                graph[team][i] = False
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
    
    if len(result) != n:
        print("IMPOSSIBLE")
        continue
    if donknow:
        print("?")
        continue
    for i in range(n):
        if i == n-1:
            print(result[i])
        else:
            print(result[i], end=" ")