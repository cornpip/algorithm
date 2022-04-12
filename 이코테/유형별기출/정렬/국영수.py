import sys
input = sys.stdin.readline

n = int(input())
# int 처리돼도 개행문자 없어진다.

student = []
for _ in range(n):
    yap = input().split()
    yap[1:4] = list(map(int, yap[1:4]))
    student.append(yap)

student.sort(key=lambda x:( -x[1], x[2], -x[3], x[0]))

for i in student:
    print(i[0])

print(student)