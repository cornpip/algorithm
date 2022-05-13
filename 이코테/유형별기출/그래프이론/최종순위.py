import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    pre = list(map(int, input().split()))

    indegree = [0] * (n+1)
    # graph = [[] for _ in range(n+1)]
    graph = [0] * (n+1)
    for i, val in enumerate(pre):
        graph[val] = pre[i+1:]
        indegree[val] = len(pre[i+1:])
        
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[b].remove(a)
            indegree[b] -= 1
            graph[a].append(b)
            indegree[a] += 1
        elif b in graph[a]:
            graph[a].remove(b)
            indegree[a] -= 1
            graph[b].append(a)
            indegree[b] += 1

    q = deque()
    for i, val in enumerate(indegree):
        if i == 0:
            continue
        if val == 0:
            q.append(i)
    result = []
    donknow = False
    while q:
        if len(q) > 1:
            donknow = True
        team = q.popleft()
        result.append(team)
        for i, ls in enumerate(graph):
            if i == 0:
                continue
            if team in ls:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
    
    if len(result) != n:
        print("IMPOSSIBLE")
        continue
    if donknow:
        print("?")
        continue
    for i in range(n-1,-1,-1):
        if i == 0:
            print(result[i])
        else:
            print(result[i], end=" ")