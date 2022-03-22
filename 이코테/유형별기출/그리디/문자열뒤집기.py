s = list(map(int, input()))

count = 0
yap = s[0]
for i in s:
    if i != yap:
        count += 1
        yap = i

result = count//2
print(result)