## 이거는 아이디어가 되게 어렵다

n = int(input())

d = [0] * 1001
d[1], d[2] = 1, 3

for i in range (3, n+1):
    d[i] = d[i-1] + d[i-2] * 2 % 796796

print(d[n])

## 밑에서 부터 값을 보면서
## 알고있는 것과 알아야할 것(=?)을 나눠서 접근해보자