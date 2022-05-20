import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int, input().split())
sea = []
for i in range(n):
    sea.append(list(map(int, input().split())))

# num만 일치시킨거임 1,2,3,4 는 0,1,2,3
arrows = list(map(int, input().split()))
priors = [[] for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(4):
        priors[i].append(list(map(int, input().split())))

# 위 아래 왼쪽 오른쪽 순서맞춰둠
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def stepbyone(sea, fish, fishs_move):
    num ,now, arrow, prior, echo = fish
    x, y = now
    possible = []
    smell =[]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx > -1 and ny < n and ny > -1:
            if sea[nx][ny] == num:
                smell.append([nx, ny, i+1])
            elif sea[nx][ny] == 0:
                possible.append([nx, ny, i+1])
            # elif type(sea[nx][ny]) == list:
            #     possible.append([nx, ny, i+1])
    if len(possible) == 1:
        n_x, n_y, n_a = possible[0]
    elif len(possible) > 1:
        yaap = False
        for i in prior:
            for j in possible:
                if i == j[2]:
                    n_x, n_y, n_a = j
                    yaap = True
                    break
            if yaap:
                break
    elif len(smell) == 1:
        n_x, n_y, n_a = smell[0]
    elif len(smell) > 1:
        yaap = False
        for i in prior:
            for j in smell:
                if i == j[2]:
                    n_x, n_y, n_a = j
                    yaap = True
                    break
            if yaap:
                break
    else:
        return [num, 0, 0, 0, echo, False]

    # sea[x][y] = num    
    fishs_move.append([num, [n_x,n_y], n_a, priors[num][n_a-1], echo])                 
    # return [num, [n_x,n_y], n_a, priors[num][n_a-1], echo, "nothing"]

# 밖에서 할꺼: 방향에 따른 우선순위, 겹치는 거 처리, 초 세기, 한마리씩 넣어주기
fishs = []
for i in range(n):
    for j in range(n):
        if sea[i][j] != 0:
            id = sea[i][j]
            arrow = arrows[id-1]
            prior = priors[id][arrow-1]
            echo = deque()
            echo.append([i,j])
            fishs.append([id, [i,j], arrow, prior, echo])
# fish = 번호 ,현재 위치, 방향, 우선순위, echo
# [2,[x,y], 2, [3,2,1,4], deque]
dead = [] # [num, q]
t=0
while 1:
    n_steps = []
    fishs_move = []
    for fish in fishs:
        n_step = stepbyone(sea, fish, fishs_move)
    sea_t = [[0] * n for _ in range(n)]
    for move in fishs_move:
        x, y = move[1]
        if sea_t[x][y] != 0:
            data = sea_t[x][y]
            if move[0] < data[0]:
                n_steps.append(move[:5])
                for i in range(len(n_steps)):
                    if n_steps[i][0] == data[0]:
                        n_steps.pop(i)
                        break
                dead.append([data[0], data[4]])
                sea_t[x][y] = move[:5]
            else:
                dead.append([move[0], move[4]])
        else:
            n_steps.append(move[:5])
            sea_t[x][y] = move[:5]
    
    for i in range(n):
        for j in range(n):
            if sea_t[i][j] != 0:
                sea[i][j] = sea_t[i][j][0]
        # return [num, [n_x,n_y], n_a, priors[num][n_a-1], echo, "nothing"]
    for i in n_steps:
        echo = i[4]
        echo.append(i[1])
        if len(echo) > k:
            d_x, d_y = echo.popleft()
            ha = False
            for i in echo:
                if i == [d_x, d_y]:
                    ha = True
                    break
            if not ha:
                sea[d_x][d_y] = 0  
    for i in dead:
        echo = i[1]
        echo.append(False)
        if len(echo) > k:
            yap = echo.popleft()
            if yap:
                d_x, d_y = yap[:2]
                ha = False
                for i in echo:
                    if i == [d_x, d_y]:
                        ha = True
                        break
                if not ha:
                    sea[d_x][d_y] = 0    
    fishs = n_steps
    t += 1
    # print(n_steps)
    # for i in range(n):
    #     print(sea[i])
    if len(n_steps) < 2:
        break
    elif t >= 1000:
        t = -1
        break

print(t)