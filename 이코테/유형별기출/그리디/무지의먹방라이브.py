food_Time = list(map(int, input().strip("[]").split(",")))
k = int(input())

index = 0
out = False
for i in range (k):
    count = 0
    while food_Time[index] == 0:
        if count == len(food_Time):
            print(-1)
            out = True
            break
        index += 1
        index %= len(food_Time)
        count += 1
    food_Time[index] -= 1
    index += 1
    index %= len(food_Time)
    count = 0
    while food_Time[index] == 0:
        if count == len(food_Time):
            print(-1)
            out = True
            break
        index += 1
        index %= len(food_Time)
        count += 1

if out == False:
    print(index + 1)

## 이렇게하면 효율성 하나도 통과안된다.