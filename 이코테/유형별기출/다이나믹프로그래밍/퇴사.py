import sys
input = sys.stdin.readline

n = int(input())
t, p = [], []
for _ in range(n):
    time, price = map(int, input().split())
    t.append(time)
    p.append(price)

dp = [0] * n

maxval = 0
for i in range(n-1, -1, -1):
    time = i + t[i]
    if time > n:
        dp[i] = maxval
    elif time == n:
        dp[i] = max(p[i], maxval)
        maxval = dp[i]
    else:
        dp[i] = max(p[i] + dp[time], maxval)
        maxval = dp[i]

print(dp[0])