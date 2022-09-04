from collections import deque

n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

# print(graph)


def dps(visited: list, s: int, res: list):
    if visited[s] == True:
        return
    visited[s] = True
    res.append(s)
    for node in graph[s]:
        dps(visited, node, res)
    return res


def bps(visited: list, s: int, res: list):
    q = deque()
    q.append(s)
    while q:
        now = q.popleft()
        if visited[now] == True:
            continue
        visited[now] = True
        res.append(now)
        for i in graph[now]:
            q.append(i)
    return res


d_res = dps([False for _ in range(n+1)], v, [])
b_res = bps([False for _ in range(n+1)], v, [])

# print(d_res)
# print(b_res)


def form(res: list):
    leng = len(res)
    for i in range(leng):
        if i == leng-1:
            print(res[i])
        else:
            print(res[i], end=" ")


form(d_res)
form(b_res)
