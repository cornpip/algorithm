import sys
input = sys.stdin.readline

def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]

def union(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    elif b<a:
        parent[a] = b

g = int(input())
p = int(input())
p_list = []
for _ in range(p):
    p_list.append(int(input()))

parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i

count = 0
for p in p_list:
    a = find_parent(parent, p)
    if a == 0:
        break
    union(parent, a, a-1)
    count += 1

print(count)