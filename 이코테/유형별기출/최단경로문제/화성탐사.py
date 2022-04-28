import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
T = int(input())

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
            continue
        result[x][y] = energy
        if x == n-1 and y == n-1:
            continue
        if x == 0:
            if y == 0:
                heapq.heappush(heap, [energy + geo[x][y+1], [x,y+1]])
                heapq.heappush(heap, [energy + geo[x+1][y], [x+1, y]])
            elif y == n-1:
                heapq.heappush(heap, [energy + geo[x][y-1], [x, y-1]])
                heapq.heappush(heap, [energy + geo[x+1][y], [x+1, y]])
            else:
                heapq.heappush(heap, [energy + geo[x][y-1], [x, y-1]])
                heapq.heappush(heap, [energy + geo[x][y+1], [x,y+1]])
                heapq.heappush(heap, [energy + geo[x+1][y], [x+1, y]])
        elif x == n-1:
            if y == 0:
                heapq.heappush(heap, [energy + geo[x][y+1], [x,y+1]])
                heapq.heappush(heap, [energy + geo[x-1][y], [x-1,y]])
            elif y == n-1:
                heapq.heappush(heap, [energy + geo[x][y-1], [x, y-1]])
                heapq.heappush(heap, [energy + geo[x-1][y], [x-1, y]])
            else:
                heapq.heappush(heap, [energy + geo[x][y-1], [x, y-1]])
                heapq.heappush(heap, [energy + geo[x][y+1], [x,y+1]])
                heapq.heappush(heap, [energy + geo[x-1][y], [x-1, y]])
        elif y == 0:
                heapq.heappush(heap, [energy + geo[x][y+1], [x, y+1]])
                heapq.heappush(heap, [energy + geo[x+1][y], [x+1,y]])
                heapq.heappush(heap, [energy + geo[x-1][y], [x-1, y]])
        elif y == n-1:
                heapq.heappush(heap, [energy + geo[x][y-1], [x, y-1]])
                heapq.heappush(heap, [energy + geo[x+1][y], [x+1,y]])
                heapq.heappush(heap, [energy + geo[x-1][y], [x-1, y]])
        else:
            heapq.heappush(heap, [energy + geo[x-1][y], [x-1,y]])
            heapq.heappush(heap, [energy + geo[x][y+1], [x,y+1]])
            heapq.heappush(heap, [energy + geo[x+1][y], [x+1, y]])
            heapq.heappush(heap, [energy + geo[x][y-1], [x, y-1]])

    print(result[n-1][n-1])