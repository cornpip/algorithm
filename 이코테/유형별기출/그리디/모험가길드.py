import sys
input = sys.stdin.readline

n = int(input())
n_state = list(map(int, input().split()))

n_state.sort()

count = 0
result = 0
for i in n_state:
    count += 1
    if count == i:
        result += 1
        count = 0

print(result)