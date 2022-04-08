n = int(input())

geo = []
student =[]
for i in range(n):
    geo.append(list(input().split()))
    for j in range(n):
        if geo[i][j] == "S":
            student.append((i,j))

def dfs(geo, x, y, count):
    global student
    if count == 3:
        if check(geo, student):
            return True
        else:
            return False
    while 1:
        if geo[x][y] == "X":
            geo[x][y] = "O"
            if dfs(geo, x, y, count+1): return True
            geo[x][y] = "X"
        if x+1 == n:
            x=0
            y += 1
            if y == n: return
        else:
            x += 1

def check(geo, student):
    for k in student:
        i, j = k[0], k[1]
                # 위
        count = 1
        while 1:
            if i - count == -1:
                break
            if geo[i-count][j] == "O":
                break
            if geo[i-count][j] == "T":
                return False
            count += 1
        # 아래
        count = 1
        while 1:
            if i + count == n:
                break
            if geo[i+count][j] == "O":
                break
            if geo[i+count][j] == "T":
                return False
            count += 1
        # 왼쪽
        count = 1
        while 1:
            if j - count == -1:
                break
            if geo[i][j-count] == "O":
                break
            if geo[i][j-count] == "T":
                return False
            count += 1  
        # 오른쪽
        count = 1         
        while 1:
            if j + count == n:
                break
            if geo[i][j+count] == "O":
                break
            if geo[i][j+count] == "T":
                return False
            count += 1     
    return True  

print("YES") if dfs(geo, 0, 0, 0) else print("NO")