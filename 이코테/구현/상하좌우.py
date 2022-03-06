n = int(input())
moves = input().split()
row, col = 1, 1

# restcount = len(move)

# for i in moves:
#     if(i == "U"):
#         if(row-1 == 0):
#             continue
#         row -= 1
#     if(i == "D"):
#         if(row+1 > n):
#             continue
#         row += 1
#     if(i == 'R'):
#         if(col+1 > n):
#             continue
#         col += 1
#     if(i == "L"):
#         if(col-1 == 0):
#             continue
#         col -= 1

# print(row, col)

## ======================= 위에처럼 하면 계산의 경우가 좀만 많아져도 코드량이 많다.
move_type = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for move in moves:
    for idx, val in enumerate(move_type):
        if move == val:
            nx = row + dx[idx]
            ny = col + dy[idx]
    if ( nx < 1 or ny < 1 or nx > n or ny > n):
        continue
    row, col = nx, ny

print(row, col)
