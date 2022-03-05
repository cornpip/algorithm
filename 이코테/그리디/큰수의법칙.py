# import sys
# sys.path.append("C:/Users/choi/VscodeProject/Algorithm/이코테/Package")
# import simplytime as time

n, m, k = map(int, input().split())
m2 = m
# split() == split(' ')

data = list(map(int, input().split()))
# python map자료형이 따로 있다

data.sort()
biggest = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += biggest
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)

# -------------------------------------
count = int(m2 / (k+1)) * k
count += m2 % (k+1)

result = 0
result += count * biggest
result += (m2-count) * second

print(result)
