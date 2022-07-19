# 2869

import math
a,b,v = map(int, input().split())

diff = a-b
day = math.ceil((v-a)/diff)

if diff*(day-1)+a >= v:
    print(day)
else:
    print(day+1)

# 수학 문제는 제한에 맞는 규칙찾기가 어렵다.
# 키보드보다 연필이 더 필요함