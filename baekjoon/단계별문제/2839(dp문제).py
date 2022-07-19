# 2839

dp = [int(1e9)] * 5001
dp[3], dp[5] = 1, 1
for i in range(6, 5001):
    dp[i] = min(dp[i-3]+1, dp[i-5]+1)

n = int(input())

if dp[n] >= int(1e9):
    print(-1)
else:
    print(dp[n])

# 딱 맞게 채우기 = dp 점화식