from collections import deque

n, m = map(int, input().split())

tray = []
for i in range(n):
    tray.append(input())

visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if( tray[i][j] == "1" ):
            visited[i][j] = 2

icecream = 0
check = [(-1,0),(1,0),(0,-1),(0, 1)]

def BFS(a):
    global icecream
    q.append(a)
    while q:
        v = q.popleft()
        visited[v[0]][v[1]] = True
        for i in check:
            n_row = v[0] + i[0]
            n_col = v[1] + i[1]
            if(n_row>n-1 or n_row<0 or n_col>m-1 or n_col<0):
                continue
            if(visited[n_row][n_col] == False):
                q.append([n_row, n_col])
                # BFS([n_row, n_col])
    icecream += 1
        
for i in range(n):
    for j in range(m):
        if(visited[i][j] == False):
            q = deque()
            BFS([i,j])

print(icecream)