def check(arr):
    n = len(arr)
    pre = "s"
    for i in range(n):
        for j in range(n):
            if pre != "s":
                if pre != arr[i][j]:
                    return False
            else:
                pre = arr[i][j]
    return (True, pre)

def compression(arr):
    rres = check(arr)
    if rres:
        return rres[1]
    sol = "("
    n = len(arr)
    half_n = int(n/2)
    uudd = [[],[],[],[]]
    for i in range(4):
        uudd[i] = [ [0] * half_n for _ in range (half_n) ]
    for i in range(n):
        for j in range(n):
            if i < half_n and j < half_n:
                #left_up
                # print(i,j)
                uudd[0][i][j] = arr[i][j]
            elif i < half_n and j >= half_n:
                #right_up
                uudd[1][i][j-half_n] = arr[i][j]
            elif i >= half_n and j < half_n:
                #left_down
                uudd[2][i-half_n][j] = arr[i][j]
            elif i >= half_n and j >= half_n:
                #right_down
                uudd[3][i-half_n][j-half_n] = arr[i][j]

    for part in uudd:
        if len(part) == 1:
            sol += str(part[0][0])
            continue

        res = check(part)
        if not res:
            # print(part)
            cir = compression(part)
            sol += cir
        else:
            sol += str(res[1])
    sol += ")"
    return sol

n = int(input())
arr = []
for i in range(n):
    row = list(map(int, input()))
    # print(row)
    arr.append(row)

print(compression(arr))