from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range (n):
    graph.append(list(map(int, input())))

print(graph)

check = [(-1, 0), (1, 0), (0, -1), (0, 1)]

first = [0, 0, 1]  ##  0 0으로 받았다 주의

def BFS(a):
    q = deque()
    q.append(a)
    new_now = [0, 0, 0]
    while q:
        now = q.popleft()
        graph[now[0]][now[1]] = 2
        if ( now[0] == n-1 and now[1] == m-1 ):
            print(new_now[2])
            break
        for move in check:
            next_r = now[0] + move[0]
            next_c = now[1] + move[1]
            if ( -1 < next_r < n and -1 < next_c < m and graph[next_r][next_c] == 1):
                new_now = [next_r, next_c, now[2] + 1]
                q.append(new_now)

BFS(first)
print(graph)