n, m = map(int, input().split())

yap = list(map(int, input().split()))
dynamic = [0] * (m+1)
for i in yap:
    dynamic[i] += 1

def combination(n):
    result = int(n*(n-1)/2)
    return result

all_count = 0
# for  i in range(1, m+1):
#     count = 0
#     for j in yap:
#         if j == i:
#             count += 1
#     if count >= 2:
#         aa = combination(count)
#         all_count += aa

for i in dynamic:
    if i >= 2:
        all_count += combination(i)

result = combination(n) - all_count
print(result)
