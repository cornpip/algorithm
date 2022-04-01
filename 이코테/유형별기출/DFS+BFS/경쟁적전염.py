from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

l_q=[]
for _ in range(k):
    l_q.append(deque())

geo = []
for _ in range(n):
    geo.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        yap = geo[i][j]
        if yap != 0:
            l_q[yap-1].append((i,j))

s, x, y = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sec = 0
while 1:
    if sec == s: break
    for index ,q in enumerate (l_q):
        for i in range(len(q)):
            covid = q.popleft()
            for num in range(4):
                nx = covid[0] + dx[num]
                ny = covid[1] + dy[num]
                if -1 < nx < n and -1 < ny < n:
                    if geo[nx][ny] == 0:
                        geo[nx][ny] = index+1
                        q.append((nx, ny))
    sec += 1

print(geo[x-1][y-1])