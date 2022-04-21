import sys
input = sys.stdin.readline

def aaa(matrix,row,col):
    if matrix[row][col] != -1:
        return matrix[row][col]

    if col == 0:
        return gold_map[row][col]

    if row == 0:
        max_result = max( aaa(matrix, row, col-1), aaa(matrix, row+1, col-1))
    elif row == n-1:
        max_result = max( aaa(matrix, row, col-1), aaa(matrix, row-1, col-1))
    else:
        max_result = max( aaa(matrix, row, col-1), aaa(matrix, row+1, col-1), aaa(matrix, row-1, col-1))
    
    matrix[row][col] = max_result + gold_map[row][col] 
    return max_result + gold_map[row][col]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    gold_map = [[] for _ in range(n)]
    yap = list(map(int, input().split()))

    count = 0
    for i, val in enumerate(yap):
        if i % m == 0 and i != 0:
            count += 1
        gold_map[count].append(val)
    
    matrix = [[-1] * m for _ in range(n)]
    result = -1
    for i in range(n):
        result = max(result, aaa(matrix, i, m-1))
    print(result)
    print(matrix)