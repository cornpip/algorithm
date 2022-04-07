from itertools import permutations

n = int(input())

num_l = list(map(int, input().split()))
calcul = list(map(int, input().split()))

def calculation(prev, next, cal):
    result=0
    yap = 0
    if cal == 0:
        result = prev + next
    elif cal == 1:
        result = prev - next
    elif cal == 2:
        result = prev * next
    elif cal == 3:
        if prev < 0:
            prev = abs(prev)
            yap = 1
        result = prev // next
        if yap:
            result = -result
    return result

calcul2 = []
for i,val in enumerate(calcul):
    for _ in range(val):
        calcul2.append(i)

max_result = -1e9
min_result = 1e9
for i in permutations(calcul2):
    for j, val in enumerate(num_l):
        if j == 0:
            prev = val
            continue
        prev = calculation(prev, val, i[j-1])
    if prev > max_result:
        max_result = prev
    if prev < min_result:
        min_result = prev

print(max_result)
print(min_result)