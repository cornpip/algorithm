from audioop import reverse


n, k = map(int, input().split())

arr = []
for i in range(2):
    arr.append(list(map(int, input().split())))

for i in range(k):
    if min(arr[0]) >= max(arr[1]):
        break

    if min(arr[0]) < max(arr[1]):
        a_index = arr[0].index(min(arr[0]))
        b_index = arr[1].index(max(arr[1]))
        arr[0][a_index], arr[1][b_index] = arr[1][b_index], arr[0][a_index]

print(sum(arr[0]))

# sort로 하면 2NlogN + K
# min, max로 하면 2NK
# 인 듯하다. N과 K가 크다면 sort가 올바른 풀이다.

# 쉬운 문제도 허용된 범위에서 큰 수가 들어온다 가정하고 나은 방법을 택하자.

## sort
# arr[0].sort()
# arr[1].sort( reverse =True)

# for i in range(k):
#     if arr[0][i] < arr[1][i]:
#         arr[0][i], arr[1][i] = arr[1][i], arr[0][i]
#         continue

#     if arr[0][i] >= arr[1][i]:
#         break

# print(sum(arr[0])) 