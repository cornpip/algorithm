import sys
input = sys.stdin.readline

n = int(input())

house = list(map(int, input().split()))
house.sort()

if n%2 == 0:
    print(house[n//2-1])
else:
    print(house[n//2])


# 만약 완전으로 간다면 당연히 시간초과
# sum_min = 1e9
# min_index = 0
# for i,now in enumerate(house):
#     sum = 0
#     for j in house:
#         if j == now:
#             continue
#         sum += abs(now-j)
#     if sum < sum_min:
#         sum_min = sum
#         min_index = i

# print(house[min_index])