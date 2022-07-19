#1978

import math
n = int(input())
ll = list(map(int,input().split()))

count = n
for i in ll:
    if i == 1:
        count -= 1
        continue
    sq_i = int(math.sqrt(i))
    for j in range(2, sq_i+1):
        if i%j == 0:
            count-=1
            break

print(count)
