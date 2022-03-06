n = int(input())

count = 0
for i in range (n+1):
    for j in range (60):
        for k in range (60):
            t = str(i)+"시 "+str(j)+"분 "+str(k)+"초"
            if "3" in t:
                count += 1

print(count)