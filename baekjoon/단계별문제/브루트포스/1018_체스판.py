def reverse(pre):
    if pre == "W":
        return "B"
    else:
        return "W"

def check(rows_cut):
    count, flag = 0, "W"
    for idx ,row_cut in enumerate(rows_cut):
        if idx != 0:
            flag = reverse(flag)
        # print(row_cut, "____", flag)
        for i in range(8):
            if i == 0:
                if row_cut[i] != flag:
                    count += 1
                now = reverse(flag)
            else:
                if row_cut[i] != now:
                    count += 1
                now = reverse(now)
    
    if 64-count > 32:
        return count
    else:
        return 64-count
    # 뒤집고 돌려볼 필요없다.
    
    # count_1 = count
    # if count_1 == 0: return 0

    # count, flag = 0, "B"
    # for idx ,row_cut in enumerate(rows_cut):
    #     if idx != 0:
    #         flag = reverse(flag)
    #     for i in range(8):
    #         if i == 0:
    #             if row_cut[i] != flag:
    #                 count += 1
    #             now = reverse(flag)
    #         else:
    #             if row_cut[i] != now:
    #                 count += 1
    #             now = reverse(now)
    # count_2 = count

    # if count_1 < count_2:
    #     return count_1
    # else:
    #     return count_2

n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(input())

n_, m_ = n-8, m-8
res = 1e9
for i in range(n_ + 1):
    for j in range(m_ + 1):
        rows = board[i:i+8]
        rows_cut = []
        for row in rows:
            rows_cut.append(row[j:j+8])
        y = check(rows_cut)
        if y < res:
            res = y

print(res)