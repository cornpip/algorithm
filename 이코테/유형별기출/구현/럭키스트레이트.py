a = list(map(int, input()))
length = int(len(a)/2)

res1 = 0
for i in range(length):
    res1 += a[i]

res2 = 0
for i in range(length, 2*length):
    res2 += a[i]

if (res1 == res2):
    print("LUCKY")
else:
    print("READY")