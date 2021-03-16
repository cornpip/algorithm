n = int(input())

for i in range(1,n):
    a = str(i)
    b = len(a)
    c = 0
    for j in range(b):
        c += int(a[j])
    if n == i + c:
        print(i)
        break
    if i == n-1:
        print('0')
if n==1:
    print('0')
        


