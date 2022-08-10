import random
from time import time

a = []
for i in range(19999999):
    a.append(random.randint(1,9))

start = time()
for i, val in enumerate (a):
    if i % 1000 == 0:
        print(i)
end = time()
first = end - start


start = time()
a = tuple(a)
for i, val in enumerate (a):
    if i % 1000 == 0:
        print(i)
end = time()
second = end - start

print(f"list: {first},  tuple: {second}")

# tuple 변환은 그렇게 시간이 들지않는다.
# 변환해서 튜플로 iteration 돌리는게 더 빠른 듯 하다.

# 모든 list요소를 tuple로 변환은 X
# ex) [[1,2],[3,4].....] => [(1,2),(3,4).....]