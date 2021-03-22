n = int(input())
s = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = []
for i in range(n):
    s.append(list(input()))
print(s)    
def bfs(i, j):
    queue = [[i, j]]
    s[i][j] = "0"
    count = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and s[x][y] == "1":
                s[x][y] = "0"
                queue.append([x, y])
                count += 1
    cnt.append(count)
for i in range(n):
    for j in range(n):
        if s[i][j] == "1":
            bfs(i, j)
cnt.sort()
print('hi')
print(len(cnt))
print(cnt)
for i in cnt:
    print(i)

    
