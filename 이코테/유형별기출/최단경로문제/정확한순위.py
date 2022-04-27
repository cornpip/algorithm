import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = "B"

def right(q, center):
    for j in range(1, n+1):
        if graph[center][j] == "B":
            q.append(j)

def left(q, center):
    for j in range(1, n+1):
        if graph[j][center] == "B":
            q.append(j)

result = 0
for i in range(1, n+1):
    visit = [[0] * (n+1) for _ in range(n+1)]
    count = 0
    q = deque()
    right(q, i)
    while q:
        stu = q.popleft()
        if visit[stu] == True:
            continue
        visit[stu] = True
        count += 1
        right(q, stu)
    
    left(q, i)
    while q:
        stu = q.popleft()
        if visit[stu] == True:
            continue
        visit[stu] == True
        count += 1
        left(q, stu)
    if count == n-1:
        result += 1

print(result)