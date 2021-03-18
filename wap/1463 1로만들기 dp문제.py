n = int(input())

count = [0,0]

for i in range(2, n+1):
    count.append(count[i-1]+1)

    if i % 2 == 0 :
        count[i] = min(count[i], count[i//2]+1)
        # 먼저 -1 하고 구한것과 먼저 2로 나누고 구한것비교

    if i % 3 == 0 :
        count[i] = min(count[i], count[i//3]+1)
        # 위에서 들어온 것과 먼저 3으로 나눈것 비교

print(count[-1])
        


