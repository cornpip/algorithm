n, m = map(int, input().split())

d = [0] * 10001
unit = []
for i in range (n):
    a = int(input())
    unit.append(a)
    d[a] = 1

minimum = min(unit)

def yap(i):
    if i < minimum:
        return 0

    return d[i]

for i in range(minimum, m + 1):
    hmm = 999
    if d[i] != 0:
        continue

    for j in unit:
        if yap(i-j) != 0 and yap(i-j) != -1:
            hmm = min(hmm, yap(i-j))
        else:
            continue
    
    if hmm == 999:
        d[i] = -1
    else:
        d[i] = hmm + 1

print(d[m])