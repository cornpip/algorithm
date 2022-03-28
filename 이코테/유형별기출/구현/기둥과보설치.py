def check(new_x,new_y,graph):
    if new_x < 0:
        return True
    if len(graph[new_x][new_y]) < 1:
        return True # 존재하지 않을 땐 문제없음
    ## ------------- 일단 있는건 확인됨
    # print(graph[new_x][new_y])
    if graph[new_x][new_y][0][0] == 1:
        # 일단 바닥에 보를 설치하는 경우는 없으므로 아래 기둥체크는 out range 안걸림
        # 아 있는지 없는지 여부에서 걸리겠네
        # 고려할 거 2가지 
        # 1. out범위인지 
        # 2. 있는지 없는지
        if not len(graph[new_x+1][new_y-1]) < 1:
            if graph[new_x+1][new_y-1][0][0] == 0:
                return True
        if not len(graph[new_x][new_y-1]) < 1:
            if graph[new_x][new_y-1][0][0] == 0:
                return True
        
        if not new_x-1 < 0:
            if not ( len(graph[new_x-1][new_y]) < 1 or len(graph[new_x+1][new_y]) < 1 ):
                if (graph[new_x-1][new_y][0][0] == 1 and graph[new_x+1][new_y][0][0] == 1):
                    return True
        # if graph[new_x+1][new_y-1][0] == 0 or graph[new_x][new_y-1][0] == 0 or (graph[new_x-1][new_y][0] == 1 and graph[new_x+1][new_y][0] == 1):
        #     return True
    else :
        if new_y == 0:
            return True
        if not new_x-1 < 0:
            if not len(graph[new_x-1][new_y]) < 1:
                if graph[new_x-1][new_y][0][0] == 1:
                    return True
        if not new_y-1 < 0:
            if not len(graph[new_x][new_y-1]) < 1:
                if graph[new_x][new_y-1][0][0] == 0:
                    return True
        # if graph[new_x-1][new_y][0] == 1 or graph[new_x][new_y-1][0] == 0:
        #     return True
    return False

## 행열이 아니라 x, y 다 주의
def solution(n, works):
    graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
    result = []
    for i_work in works:
        x, y, c, e = i_work[0], i_work[1], i_work[2], i_work[3]
        # print(x,y,c,e)
        if e == 1:
            if c == 1:
                new_x, new_y = x+1, y
            if c == 0:
                new_x, new_y = x, y+1
            graph[x][y].append((c,new_x,new_y))
            if not check(x,y,graph):
                graph[x][y].pop()
            else:
                result.append([x,y,c])
        elif e == 0:
            if c == 1:
                new_x, new_y = x+1, y
                two_x, two_y = x-1, y
            if c == 0:
                new_x, new_y = x, y+1
                two_x, two_y = x-1, y+1
            keep = graph[x][y].pop() # 없는 구조물을 삭제하는 경우는 없다.
            if not ( check(new_x, new_y, graph) and check(two_x, two_y, graph) ):
                graph[x][y].append(keep)
            else:
                result.remove([x,y,c])
        # print(result)
    result.sort()
    return result

# 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없다.
# 보와 기둥을 동시에 설치하는 경우는 없다 ( 구조물이 겹치도록 설치하는 경우는 주어지지않는다. )

yap = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(5, yap))