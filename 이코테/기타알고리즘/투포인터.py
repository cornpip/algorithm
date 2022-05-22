n = list(map(int, input().split()))
m = int(input())

count = 0
t_sum = 0
end = 0
res = []
t_res = []

for start in range(len(n)):
    while t_sum < m and end < len(n):
        t_sum += n[end]
        t_res.append(n[end])
        end += 1
    if t_sum == m:
        count += 1
        res.append([i for i in t_res]) # 이런 copy해야하는 부분들 주의
    t_sum -= n[start]
    t_res.pop(0)

print(count)
print(res)