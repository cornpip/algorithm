from collections import deque

n, m = map(int, input().split())
geo = []
for i in range(n):
    line = list(map(int, input()))
    geo.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append([0, 0, 0, visited])
    while q:
        x, y, count, visited = q.popleft()
        if visited[x][y] == True:
            print("동일level 동일count 차단", x, y, count)
            continue
        # print("안 들린거", x,y,count)
        visited[x][y] = True
        count += 1
        if x == n-1 and y == m-1:
            return count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if visited[nx][ny] == True or geo[nx][ny] == 0:
                    continue
                # [ i[:] for i in visited ]
                q.append([nx, ny, count, visited])


print(bfs())
