# Top-Down
d = [0] * 100

def Top_Down(x):
    if x == 1 or x== 2:
        return 1

    if d[x] != 0:
        return d[x]
    
    # print(x)
    d[x] = Top_Down(x-1)+Top_Down(x-2)
    return d[x]

print(Top_Down(99))

# Bottom-Up
d = [0] * 100

n = 99
d[1], d[2] = 1, 1
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])