import sys
import heapq
input =sys.stdin.readline

arrow = [[] for _ in range(4)]
fish = [[] for _ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(8):
        if j % 2 == 0:
            arrow[i].append(line[j])
        else:
            fish[i].append(line[j])

fish[0][0] = -1 #상어 (보류)
shark = [0, 0]
xx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
yy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def run(fish, arrow):
    global shark
    q = [] 
    for i in range(4):
        for j in range(4):
            if i==shark[0] and j==shark[1]:
                continue
            heapq.heappush(q, [fish[i][j], i, j])
    while q:
        num, x, y = heapq.heappop(q)
        while 1:
            mv = arrow[x][y]
            nx = x + xx[mv]
            ny = y + yy[mv]
            if nx > -1 and nx < 4 and ny > -1 and ny < 4 and [nx, ny] == shark:
                fish[nx][ny], fish[x][y] = fish[x][y], fish[nx][ny]
                arrow[nx][ny], arrow[x][y] = arrow[x][y], arrow[nx][ny]
                break # 일단 이동못할 수 있는 경우는 없다고 생각
            else:
                if mv == 8:
                    arrow[x][y] = 1
                else:
                    arrow[x][y] += 1

def yammy(fish, arrow):
    global shark