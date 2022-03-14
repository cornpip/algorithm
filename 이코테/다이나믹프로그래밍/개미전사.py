import sys
from collections import deque

n = int(input())
food = sys.stdin.readline().rstrip()
food = list(map(int, food.split()))

d = [0] * 101

q_food = deque(food)
q_food.appendleft(0)
d[1] = q_food[1]

for i in range(2, n+1):
    d[i] = max(d[i-1], d[i-2] + q_food[i])

print(d[n])