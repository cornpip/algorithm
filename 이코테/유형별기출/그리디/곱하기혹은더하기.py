yap = list(map(int, input()))

result = yap[0]
for i in range (1, len(yap)):
    if yap[i] == 0 or yap[i] == 1 or result <= 1:
        result += yap[i]
    else:
        result *= yap[i]

print(result)