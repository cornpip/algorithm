import sys
import heapq
input = sys.stdin.readline

def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]

def union(parent, a, b, money):
    global res
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a
    elif a == b:
        res += money

n, m = map(int, input().split())
q = []
parent = [0] * (n+1)
res = 0
for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a, b, money = map(int, input().split())
    heapq.heappush(q, [money, a, b])

while q:
    money, a, b = heapq.heappop(q)
    union(parent, a, b, money)

print(res)