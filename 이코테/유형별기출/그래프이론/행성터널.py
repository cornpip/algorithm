import sys
import heapq
input =sys.stdin.readline

def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]

res = 0
def union(parent, a, b, dis):
    global res
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
        res += dis
    elif a > b:
        parent[a] = b
        res += dis
n = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

xl, yl, zl = [], [], []
for i in range(1, n+1):
    x,y,z = map(int, input().split())
    xl.append([x,i])
    yl.append([y,i])
    zl.append([z,i])

xl.sort(), yl.sort(), zl.sort()
q = []
xyzl = [xl, yl, zl]
for i in range(n-1):
    for j in range(3):
        heapq.heappush(q, ( xyzl[j][i+1][0]-xyzl[j][i][0], xyzl[j][i+1][1], xyzl[j][i][1]))

while q:
    dis, v1, v2 = heapq.heappop(q)
    union(parent, v1, v2, dis)

print(res)