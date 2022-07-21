from bisect import bisect_right

dp = [0] * 10001
so = []
for i in range(2, 10001):
    if dp[i] == 0:
        so.append(i)
        up = 1
        while 1:
            x = i * up
            if x > 10000:
                break
            dp[x] = -1
            up += 1

t = int(input())
for i in range(t):
    n = int(input())
    line = bisect_right(so, n/2)
    for i in range(line-1, -1, -1):
        a = so[i]
        if n-a in so:
            print(a, n-a)
            break

# 에라토스테네스 체 쓸 때
# 소수도 그냥 위치랑 똑같게 테이블 가지고 있는게 낫겠네
# so[2] == 1 : 2는 소수다