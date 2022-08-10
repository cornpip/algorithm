# 1991

n = int(input())
mm = [[] for _ in range(n)]

for i in range(n):
    a, b, c = input().split()
    mm[ord(a)-65] = [a, b, c]

a,b,c = [0,1,2],[1,0,2],[1,2,0]

def bb(f, ll, res):
    global mm
    if f == [0,1,2]:
        for i in f:
            if i == 0:
                res.append(ll[i])
                continue
            idx = ord(ll[i])-65
            if idx == -19:
                continue
            bb(f, mm[idx], res)
    else:
        for i in f:
            if i == 0:
                res.append(ll[i])
                continue
            idx = ord(ll[i])-65
            if idx == -19:
                continue
            bb(f, mm[idx], res)

yap = [a,b,c]
for i in range(3):
    res = []
    bb(yap[i], mm[0], res)
    print(''.join(res))