import heapq
import sys
input = sys.stdin.readline

n = int(input())

card =[]
for _ in range(n):
    heapq.heappush(card, int(input()))

result = 0
while len(card) > 1:
    one = heapq.heappop(card)
    two = heapq.heappop(card)
    result += one+two
    heapq.heappush(card, (one+two))

print(result)