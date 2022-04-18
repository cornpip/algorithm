import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()

def search(arr, min_gap, max_gap):
    while max_gap >= min_gap:
        mid_gap = (max_gap + min_gap)//2
        count = 1
        index = 0
        for i in range(1, n):
            if arr[i]-arr[index] >= mid_gap:
                index = i
                count += 1
        if count < c:
            max_gap = mid_gap -1
        if count >= c:
            min_gap = mid_gap + 1
            result = mid_gap
    return result

s_val, e_val = house[0], house[-1]
max_gap = e_val-s_val
min_gap = 1

print(search(house, min_gap, max_gap))