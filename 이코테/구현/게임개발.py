from unittest import mock


n, m = map(int, input().split())
a, b, now_arrow = map(int, input().split())

mapinfo = []
for i in range(n):
    mapinfo.append(list(map(int, input().split())))

next = {"0":3, "3":2, "2":1, "1":0}

BackMove = [(1, 0), (0, -1), (-1, 0), (0, 1)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

move_count =  0
check_count = 0

while 1:
    if(check_count == 4):
        n_a = a + BackMove[now_arrow][0]
        n_b = b + BackMove[now_arrow][1]
        if( -1<n_a<n+1 and -1<n_b<m+1 and mapinfo[n_a][n_b] != 1):
            mapinfo[a][b] = 2
            a = n_a
            b = n_b
            move_count += 1
            check_count = 0
            # print(a, b)
            continue
        else:
            break
    now_arrow = next[str(now_arrow)]
    n_a = a + move[now_arrow][0]
    n_b = b + move[now_arrow][1]
    if( -1<n_a<n+1 and -1<n_b<m+1 and mapinfo[n_a][n_b] == 0):
        mapinfo[a][b] = 2 #떠난 자리
        # mapinfo[n_a][n_b] = 2 # 방문여부
        a = n_a
        b = n_b
        move_count += 1
        check_count = 0
        # print(a, b)
        continue
    check_count += 1
    print(a, b, "check: ",check_count)

print(move_count)