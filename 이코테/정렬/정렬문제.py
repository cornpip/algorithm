# 위에서 아래로
# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# arr.sort(reverse=True)
# print(arr)

# for i in arr:
#     print(i, end=" ")

# 성적이 낮은 순서로 학생 출력하기
n = int(input())

arr = []
for i in range (n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr.sort(key=lambda a: a[1])
arr2 = [ x[0] for x in arr ]

for i in arr2:
    print(i, end=" ")