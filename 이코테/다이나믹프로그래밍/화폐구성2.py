n, m = map(int, input().split())

unit = []
for i in range (n):
    a = int(input())
    unit.append(a)

d = [999] * (m+1)
d[0] = 0

for i in unit:
    for j in range(i, m+1):
        if d[j-i] != 999:
            d[j] = min(d[j], d[j-i] + 1)

if d[m] == 999:
    print(-1)
else:
    print(d[m])