import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+2)
for i in range(1, n+2):
    parent[i] = i

for i in range(m):
    z, a, b = map(int, input().split())
    if z == 0:
        union_parent(parent, a, b)
    
    if z == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

# 이거 출력이 입력마다 나오는데 예시코드도 같은걸보면 상관없는 듯 보인다.