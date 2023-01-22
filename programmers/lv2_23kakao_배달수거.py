import time

# slice를 왜 꼭 넣을려했지??
def move_process(dist, cap, some_list):
    # 들어온 시점에서 clear가 아닌거
    trick = -1
    clear = False
    while 1:
        val = some_list[dist]
        if not cap:
            trick = dist+1
            break

        if val or dist == 0:
            if cap-val < 0:
                some_list[dist] -= cap
                cap = 0
                if dist == 0:
                    trick = 0
            else:
                cap -= val
                some_list[dist] = 0
                if dist == 0:
                    clear = True
                    cap = 0
        dist -= 1
    return some_list, clear, trick


def solution(cap, n, deliveries, pickups):
    d_clear, p_clear = False, False
    total_move = 0
    d_index, p_index = n-1, n-1
    while 1:
        hd_index, hp_index = -1, -1
        while not d_clear:
            d = deliveries[d_index]
            if d:
                hd_index = d_index
                deliveries, d_clear, trick = move_process(
                    d_index, cap, deliveries)
                if trick != -1:
                    d_index = trick
                break
            else:
                if d_index == 0:
                    d_clear = True
                d_index -= 1
        while not p_clear:
            p = pickups[p_index]
            if p:
                hp_index = p_index

                pickups, p_clear, trick = move_process(
                    p_index, cap, pickups)
                if trick != -1:
                    p_index = trick
                break
            else:
                if p_index == 0:
                    p_clear = True
                p_index -= 1

        if hd_index==-1 and hp_index==-1:
            pass
        else:
            total_move += 2*(hd_index+1) if hd_index >= hp_index else 2*(hp_index+1)
        
        # time.sleep(1)
        # print(hd_index, hp_index, total_move, d_clear, p_clear)
        if d_clear and p_clear:
            break

    return total_move

res = solution(2, 7, [1,0,2,0,1,0,2], [0, 2, 0, 1, 0, 2, 0])
# res = solution(2, 2, [0, 6], [0, 0])
# res = solution(5, 3, [0,0,0], [0,0,0])
print(res)
