import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
T = int(input())


dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(T):
    n = int(input())
    geo = []
    for _ in range(n):
        geo.append(list(map(int, input().split())))
    
    result = [[INF] * n for _ in range(n)]
    result[0][0] = geo[0][0]
    heap = []
    heapq.heappush(heap, [geo[0][0] + geo[0][1],[0,1]])
    heapq.heappush(heap, [geo[0][0] + geo[1][0],[1,0]])
    while heap:
        energy, now = heapq.heappop(heap)
        x, y = now[0], now[1]
        if result[x][y] < energy:
            # 이게 아래에서 거르고 result에 값넣고 push하면
            # 여기 걸릴 경우가 없다고 생각이드는데 일단 다익스트라 코드에서도 여기 조건 걸어놨으니까
            # 안전으로 걸어는 두자

            # 맨 첫 pop에서 같은 목적지 비용다른 경우 있다면 필요
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                cost = energy + geo[nx][ny]
                if (cost) < result[nx][ny]:
                    result[nx][ny] = cost
                    heapq.heappush(heap, [cost, [nx, ny]])  

    print(result[n-1][n-1])