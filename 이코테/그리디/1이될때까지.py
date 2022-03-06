# import sys
# sys.path.append("C:/Users/choi/VscodeProject/Algorithm/이코테/Package")
# import simplytime as time

n, k = map(int, input().split())
count = 0
count2 = 0

while 1:
    count2 += 1
    if(n == 1):
        break
    if(n < k):
        count += n-1
        break
    if(n % k == 0):
        n /= k
        count += 1
    elif( n % k != 0):
        n -= 1
        count += 1
print(count)
print(count2)