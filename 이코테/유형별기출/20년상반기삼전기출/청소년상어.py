import sys
import heapq
input =sys.stdin.readline

arrow = [[] for _ in range(4)]
fish = [[] for _ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(8):
        if j % 2 == 0:
            fish[i].append(line[j])
        else:
            arrow[i].append(line[j])

ate = fish[0][0]
fish[0][0] = -1 #상어
shark = [0, 0]
xx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
yy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def run(fish, arrow, shark):
    q = [] 
    for i in range(4):
        for j in range(4):
            if i==shark[0] and j==shark[1]:
                continue
            heapq.heappush(q, fish[i][j])
    while q:
        num = heapq.heappop(q)
        locate = []
        for i in range(4):
            for j in range(4):
                if fish[i][j] == num:
                    locate = [i, j]
        x, y = locate
        # print("~~~~~~q:", fish,"num ", num)
        while 1:
            mv = arrow[x][y]
            if mv == 0:
                break
            nx = x + xx[mv]
            ny = y + yy[mv]
            if nx > -1 and nx < 4 and ny > -1 and ny < 4 and [nx, ny] != shark:
                fish[nx][ny], fish[x][y] = fish[x][y], fish[nx][ny]
                arrow[nx][ny], arrow[x][y] = arrow[x][y], arrow[nx][ny]
                break # 일단 이동못할 수 있는 경우는 없다고 생각
            else:
                if mv == 8:
                    arrow[x][y] = 1
                else:
                    arrow[x][y] += 1

def yammy(fish, arrow, ate, shark, level=0):
    # print(level, ate)
    # print("!!",fish)
    x, y = shark
    mv = arrow[x][y]
    max = ate
    finish = 0
    for i in range(1,4):
        nx = x + xx[mv] * i
        ny = y + yy[mv] * i
        if nx > -1 and nx < 4 and ny > -1 and ny < 4 and fish[nx][ny] != 0:
            shark_c = [nx, ny]
            # print("~~~~",fish, level)
            ate_c = ate + fish[nx][ny]
            fish_c = [i[:] for i in fish]
            fish_c[x][y] = 0
            arrow_c = [i[:] for i in arrow]
            arrow_c[x][y] = 0
            fish_c[nx][ny] = -1
            run(fish_c, arrow_c, shark_c)
            yap = yammy(fish_c, arrow_c, ate_c, shark_c, level+1)
            if yap > max:
                max = yap
        else:
            finish += 1
    
    if finish == 3:
        return ate
    
    # print("end=============")
    return max

# print(fish)
run(fish, arrow, shark)
# print(fish)
# print(arrow)

res = yammy(fish, arrow, ate, shark)
print(res)