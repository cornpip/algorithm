start = input()
col = int(ord(start[0])) - int(ord('a')) + 1
row = int(start[1])

steps = [(-2,-1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

count = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if( next_row < 9 and next_row > 0 and next_col < 9 and next_col > 0 ):
        count += 1

print(count)