from bisect import bisect_left, bisect_right

dp = [0] * 10001
secret = []
for i in range(2, 10001):
    if dp[i] == 0:
        secret.append(i)
        n = 1
        while 1:
            if i*n > 10000:
                break
            dp[i*n] = -1
            n += 1

m = int(input())
n = int(input())
m_i = bisect_left(secret, m)
n_i = bisect_right(secret, n)

if secret[m_i:n_i]:
    print(sum(secret[m_i:n_i]))
    print(secret[m_i])
else:
    print(-1)