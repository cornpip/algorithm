def find_parent(parent, v):
    if parent[v] != v:
        parent[v] = find_parent(parent, parent[v])
    return parent[v]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
# 같은 a, b가 또 들어오면 a == b 이므로 아무처리도 안걸림
# a b는 1부터값

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edge = []

for _ in range(n):
    edge.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

for x in range(n):
    for y in range(n):
        if edge[x][y] == 1:
            union(parent, x+1, y+1)

yap = True
root = 0
for p in plan:
    if not root:
        root = parent[p]
    else:
        if root == parent[p]:
            continue
        else:
            yap = False
            break
if yap:
    print("YES")
else:
    print("NO")