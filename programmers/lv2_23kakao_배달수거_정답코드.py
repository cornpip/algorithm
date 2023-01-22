"""
탐욕법(greedy)
[1, 0, 3, 1, 2]
[0, 3, 0, 4, 0]

뒤에서부터 시작하여 0이상 싣게될때 위치
두 배열이 넘칠때 위치에서 비움
같은 위치에서 반복가능

two pointer
시간복잡도: O(c*n)
공간복잡도: O(c*n)
"""
from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0

    deliveries_end = deque()
    pickups_end = deque()
    loads = [0, 0]
    d_index, p_index = n-1, n-1

    while d_index > -1:
        diff = loads[0] + deliveries[d_index] - cap
        if loads[0] == 0 and deliveries[d_index] > 0:
            deliveries_end.append(d_index)
        if diff <= 0:
            loads[0] += deliveries[d_index]
            deliveries[d_index] = 0
        elif diff > 0:
            deliveries[d_index] -= cap - loads[0]
            loads[0] = 0
            continue
        d_index -= 1
    while p_index > -1:
        diff = loads[1] + pickups[p_index] - cap
        if loads[1] == 0 and pickups[p_index] > 0:
            pickups_end.append(p_index)
        if diff <= 0:
            loads[1] += pickups[p_index]
            pickups[p_index] = 0
        elif diff > 0:
            pickups[p_index] -= cap - loads[1]
            loads[1] = 0
            continue
        p_index -= 1

    if len(deliveries_end) > 0 and len(pickups_end) > 0:
        min_len = len(deliveries_end) if len(deliveries_end) < len(pickups_end) else len(pickups_end)
        for _ in range(min_len):
            d_last = deliveries_end.popleft()
            p_last = pickups_end.popleft()
            answer += 2 * (p_last + 1 if p_last > d_last else d_last + 1)
        while len(deliveries_end) > 0:
            answer += 2 * (deliveries_end.popleft() + 1)
        while len(pickups_end) > 0:
            answer += 2 * (pickups_end.popleft() + 1)

    return answer

res = solution(5, 3, [0,0,0], [0,0,0])
print(res)