from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
geo = []
for _ in range(n):
    geo.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
covid = []
wall = []

for row in range(n):
    for col in range(m):
        if geo[row][col] == 2:
            covid.append((row, col))
        if geo[row][col] == 0:
            wall.append((row, col))

aaa = 0
result = 0
for combi in combinations(wall, 3):
    geo_c = copy.deepcopy(geo)
    for j in combi:
        geo_c[j[0]][j[1]] = 1
    for virus in covid:
        q = deque()
        q.append(virus)
        while q:
            now = q.popleft()
            # geo_c[now[0]][now[1]] = -1
            for i in range(4):
                v_row = now[0] + dx[i]
                v_col = now[1] + dy[i]
                if -1 < v_row < n and -1 < v_col < m:
                    # if geo_c[v_row][v_col] == 1 or geo_c[v_row][v_col] == -1 or geo_c[v_row][v_col] == 2:
                    #     continue
                    # geo_c[v_row][v_col] = 2
                    # q.append((v_row, v_col))
                    
                    # 체크할 요소 많아지면 시간차이 1s 정도 생기네
                    # 되도록이며 논리연산자 적게 나오는 쪽으로 코딩하자

                    if geo_c[v_row][v_col] == 0:
                        geo_c[v_row][v_col] = 2
                        q.append((v_row, v_col))

    count = 0
    for i in range(n):
        for j in range(m):
            if geo_c[i][j] == 0:
                count += 1
    if count > result:
        result = count

print(result)