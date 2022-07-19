# 2775

t = int(input())

dp = [[1] + [0] * 13 for _ in range(15)]
dp[0] = [i+1 for i in range(14)]

for i in range(1, 15):
    for j in range(1, 14):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
            

for i in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])

# 규칙이 있다면 중간에서 접근

# 규칙이 안보이고 처음부터 쌓을 수 밖에 없다면 dp로 접근
# dp = 한 차례전의 결과를 활용하겠다.