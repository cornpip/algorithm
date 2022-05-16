import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())
aqua = []
yammy = 0
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 9:
            start = [i, j, 2, 0, 0, 0]
        elif line[j] != 0:
            yammy += 1
    aqua.append(line)

def step(q):
    global aqua
    global yammy
    if yammy == 0:
        return False
    find = False
    find_level = 0
    eat = []
    # aqua_c = copy.deepcopy(aqua)
    aqua_c = [i[:] for i in aqua]
    while q:
        x,y,size, time, level, eated = q.popleft()
        if aqua_c[x][y] == -1:
        #     for i in range(n):
        #         print(aqua_c[i])
            continue
        aqua_c[x][y] = -1
        if find:
            if level >= find_level:
                continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue
            if aqua_c[nx][ny] != -1 and aqua_c[nx][ny] <= size:
                if 0 < aqua_c[nx][ny] < size:
                    aqua_c[nx][ny] = -1
                    if (eated + 1) == size:
                        eat.append([nx, ny, size+1, time+1, 0, 0])
                    else:
                        eat.append([nx, ny, size, time+1, 0, eated+1])
                    find = True
                    find_level = level+1
                else:
                    q.append([nx, ny, size, time+1, level+1, eated])
    if not eat:
        return False
    temp_x = False
    temp_y = -1
    idx = 0
    # print("~~~~~~~~~~~~",eat)
    if len(eat) > 1:
        for i in range(len(eat)):
            x, y, size, time, level, eated= eat[i]
            if not temp_x and type(temp_x) == bool:
                temp_x = x
                temp_y = y 
                idx = i
            elif x < temp_x:
                temp_x = x
                temp_y = y
                idx = i
            elif x == temp_x:
                if y < temp_y:
                    idx = i
    yammy -= 1
    return eat[idx]
dx = [1,0,0,-1]
dy = [0,-1,1,0]
q = deque()
t_start = start
aqua[start[0]][start[1]] = 0
q.append(start)
while 1:
    # print("!!::::::",q)
    r_start = step(q)
    if not r_start:
        break
    else:
        t_start = r_start
        aqua[t_start[0]][t_start[1]] = 0
        q.append(t_start)

# print(yammy)
# print(t_start)
print(t_start[3])