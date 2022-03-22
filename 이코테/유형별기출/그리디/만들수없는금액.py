n = input()

m = list(map(int, input().split()))

m.sort()

target = 1
for i in m:
    if i > target:
        break
    target += i

print(target)