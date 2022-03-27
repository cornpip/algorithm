def rotate_90(a):
    tup = zip(*a[::-1])
    return [list(i) for i in tup]

def check(lock):
    lock_length = len(lock) // 3
    for i in range(lock_length, 2*lock_length):
        for j in range(lock_length, 2*lock_length):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
    
    for x in range(2*n):
        for y in range(2*n):
            for _ in range(4):
                key = rotate_90(key)

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False