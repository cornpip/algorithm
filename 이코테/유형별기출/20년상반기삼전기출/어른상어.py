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
def stepbyone(sea, fish):
    num ,now, arrow, prior, echo = fish
    x, y = now
    possible = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx > -1 and ny < n and ny > -1:
            if sea[nx][ny] == 0:
                possible.append([nx, ny, i+1])
    
    if len(possible) == 0:
        n_x, n_y, n_a = echo[0]
        # 냄새가 없다면?
    elif len(possible) == 1:
        n_x, n_y, n_a = possible[0]
    else:
        for i in prior:
            for j in possible:
                if i == j[2]:
                    n_x, n_y, n_a = j
                    break

    if sea[n_x][n_y] != 0 and sea[n_x][n_y] != num:
        if num < sea[n_x][n_y]:
            bye = sea[n_x][n_y]
            sea[n_x][n_y] = num
            # echo.append([n_x,n_y,n_a])   
            # if len(echo) > k:
            #     d_x, d_y = echo.popleft()
            #     sea[d_x][d_y] = 0          
            return [num, [n_x,n_y], n_a, priors[num][n_a-1], echo, bye, True] #먼저 있던 놈이 죽음, 나온 애는 계속 진행, 먼저 있던 얘는 빼줘야됨
        else:
            # echo.append([False])
            # if len(echo) > k:
            #     d_x, d_y = echo.popleft()
            #     sea[d_x][d_y] = 0
            return [num, [n_x,n_y], 0, 0, echo, False]  #뒤에 간놈(자기가 죽음), 나오는 거 없고 먼저있던거 그대로                   

    sea[n_x][n_y] = num
    # echo.append([n_x,n_y,n_a])
    # if len(echo) > k:
    #     d_x, d_y = echo.popleft()
    #     sea[d_x][d_y] = 0   
    return [num, [n_x,n_y], n_a, priors[num][n_a-1], echo, "nothing"]
    # 에코 다빼보자

# 밖에서 할꺼: 방향에 따른 우선순위, 겹치는 거 처리, 초 세기, 한마리씩 넣어주기
fishs = []
for i in range(n):
    for j in range(n):
        if sea[i][j] != 0:
            id = sea[i][j]
            arrow = arrows[id-1]
            prior = priors[id][arrow-1]
            echo = deque()
            echo.append([i,j,arrow])
            fishs.append(id, [i,j], arrow, prior, echo)
# fish = 번호 ,현재 위치, 방향, 우선순위, echo
# [2,[x,y], 2, [3,2,1,4], deque]
dead = [] # [num, q]
while 1:
    n_steps = []
    # for i in dead:
        
    for fish in fishs:
        n_step = stepbyone(sea, fish)
        if n_step[-1] == "nothing":
            n_steps.append(n_step[:5])
        elif n_step[-1] == True:
            bye = n_step[-2]
            for i in range(len(n_steps)):
                if n_steps[i][0] == bye:
                    dead.append([bye, n_steps[i][4]])
                    n_steps.pop(i)
            n_steps.append(n_step[:5])
        elif n_step[-1] == False:
            dead.append([n_step[0], n_step[4]])
    
    for i in n_steps:
        echo = i[5]
        echo.append(i[1]+[i[2]])
        if len(echo) > k:
            d_x, d_y = echo.popleft()
            sea[d_x][d_y] = 0  
    for i in dead:
        echo = i[1]
        echo.append(False)
        if len(echo) > k:
            yap = echo.popleft()
            if yap:
                d_x, d_y = yap[:2]
                sea[d_x][d_y] = 0  
    fishs = n_steps

# echo 처음은?

# 빠져도 냄새는 바로 안없어짐 (빠진애들 모으고 따로 돌리자)
# 모든 상어 이동 후
# 한번에 냄새 제거