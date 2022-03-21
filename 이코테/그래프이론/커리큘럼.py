from collections import deque
import sys
import copy
input = sys.stdin.readline

v = int(input())

indegree = [0] * (v+1)
time = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i]=data[0]
    for j in data[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

def topology_sort():
    result = copy.copy(time)
    q = deque()

    for i in range(1,  v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, v+1):
        print(result[i])

topology_sort()

## 하위 입장에서 상위 간선을 지운다