from collections import deque

positioned = set() 
def f_command(block,board,q):
    global positioned
    n_block = []
    #상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        for j in range(2):
            x, y = block[j]
            nx = x + dx[i]
            ny = y + dy[i]
            if -1< nx < len(board) and -1 <ny<len(board):
                if board[nx][ny] == 0:
                    n_block.append((nx,ny))
        if len(n_block) == 2:
            n_block.append(block[2] + 1)
            n_block = tuple(n_block)
            q.append(n_block)
        n_block = []
        
def s_command(block,board,q):
    global positioned
    n_block = []
    # 가로
    if block[0][0] == block[1][0]:
        hmm = "right"
        if block[0][1] < block[1][1]:
            hmm = "left"
        for z in range(2):
            flag = block[z]
            for i in range(2):
                n_block.append(flag)
                if i == 0:
                    nx = flag[0] + 1
                else :
                    nx = flag[0] - 1
                ny = flag[1]
                if -1< nx < len(board) and -1 <ny<len(board):
                    if hmm == "left":
                        if z == 0:
                            if board[nx][ny+1] == 1:
                                n_block = []
                                continue
                        else:
                            if board[nx][ny-1] == 1:
                                n_block = []
                                continue
                    else :
                        if z == 0:
                            if board[nx][ny-1] == 1:
                                n_block = []
                                continue
                        else:
                            if board[nx][ny+1] == 1:
                                n_block = []
                                continue
                    if board[nx][ny] == 0:
                        n_block.append((nx,ny))
                        n_block.append(block[2] + 1)
                        n_block = tuple(n_block)
                        q.append(n_block)
                n_block = []  
    # 세로
    if block[0][1] == block[1][1]:
        hmm = "up"
        if block[0][0] > block[1][0]:
            hmm = "down"
        for z in range(2):
            flag = block[z]
            for i in range(2):
                n_block.append(flag)
                if i == 0:
                    ny = flag[1] + 1
                else :
                    ny = flag[1] - 1
                nx = flag[0]
                if -1< nx < len(board) and -1 <ny<len(board):
                    if hmm == "down":
                        if z == 0:
                            if board[nx-1][ny] == 1:
                                n_block = []
                                continue
                        else:
                            if board[nx+1][ny] == 1:
                                n_block = []
                                continue
                    else :
                        if z == 0:
                            if board[nx+1][ny] == 1:
                                n_block = []
                                continue
                        else:
                            if board[nx-1][ny] == 1:
                                n_block = []
                                continue
                    if board[nx][ny] == 0:
                        n_block.append((nx,ny))
                        n_block.append(block[2] + 1)
                        n_block = tuple(n_block)
                        q.append(n_block)
                n_block = []

def solution(board):
    goal = len(board) - 1
    q = deque()
    q.append(((0,0),(0,1),0))
    while q:
        block = q.popleft()
        if block[0][0] == goal and block[0][1] == goal or ( block[1][0] == goal and block[1][1] == goal ):
            return block[2]
        yap = set([block[0:2]])
        if len(yap & positioned) == 1:
            continue
        positioned.update([block[0:2]])
        f_command(block, board, q)
        s_command(block, board, q)


a = solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
print(a)
# print(positioned)