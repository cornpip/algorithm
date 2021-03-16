n = int(input())
com = []

for i in range(n):
    a = input()
    com.append(a)

for i in range(n):
    mm = len(com[i])
    hap = 0
    for j in range(mm):
        if com[i][j] == '(' :
            hap += 1
        elif com[i][j] == ')':
            hap -= 1
        if hap < 0 :
            print('NO')
            break
    if hap > 0:
        print('NO')
    elif hap == 0:
        print('YES')
            
        


