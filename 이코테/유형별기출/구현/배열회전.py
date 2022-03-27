def rotate_90_zero(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def rotate_90_one(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            result[j][n-i+1] = a[i-1][j-1]
    return result

def rotate_90_zip(a):
    tup = zip(*a[::-1])
    return [list(i) for i in tup]
    # 열이 행이 되는 걸 이용
    # zip함수에 *를 붙여서 2차원 리스트를 입력하면 col끼리 tuple로 엮어준다.
    # 순서만 반대되야하므로 먼저 뒤집고 zip

test = [[1,2,3],[5,6,1],[3,5,2],[33,5,7]]
# print(test)
# print(rotate_90_one(test))
# print(rotate_90_zero(test))
print(rotate_90_zip(test))