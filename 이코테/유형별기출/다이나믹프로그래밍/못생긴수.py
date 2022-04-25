n = int(input())

dp = [0] * n
dp[1] = 1

i2, i3, i5 = 0, 0, 0
val2, val3, val5 = 2,3,5

for i in range(1,n):
    dp[i] = min(val2, val3, val5)
    if dp[i] == val2:
        i2 += 1
        val2 = dp[i2] * 2
    if dp[i] == val3:
        i3 += 1
        val3 = dp[i3] * 3
    if dp[i] == val5:
        i5 += 1
        val5 = dp[i5] * 5

print(dp[n-1])