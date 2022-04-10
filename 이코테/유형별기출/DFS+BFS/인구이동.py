from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
geo = []
for _ in range(n):
    geo.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def check(x,y):
    yap = []
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if -1<nx<n and -1<ny<n:
            if l<= abs(geo[x][y] - geo[nx][ny]) <= r:
                yap.append((nx, ny))
    return yap

# start = (0,0)
def bfs(start):
    global geo_t
    union = []
    hap = 0
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        if geo_t[x][y] == 1:
            continue
        union.append((x,y))
        hap += geo[x][y]
        geo_t[x][y] = 1
        union_c = check(x, y)
        for i in union_c:
            q.append(i)
    return union, hap

count = 0
while 1:
    result = []
    geo_t = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if geo_t[i][j] == 1:
                continue
            ho, hap = bfs((i,j))
            if len(ho) > 1:
                result.append((ho,hap))
    if not result:
        break
    for i in result:
        # print(i)
        for x, y in i[0]:
            geo[x][y] = i[1]//len(i[0])
    count += 1

print(count)