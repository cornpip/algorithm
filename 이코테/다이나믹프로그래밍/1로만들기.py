x = int(input())

d = [0] * 30001

# 바텀업
for i in range(2, x+1):
    d[i] = d[i-1] + 1
    
    if(i%5 == 0):
        d[i] = min(d[i], d[i//5] + 1)

    if(i%3 == 0):
        d[i] = min(d[i], d[i//3] + 1)
    
    if(i%2 == 0):
        d[i] = min(d[i], d[i//2] + 1)

print(d[x])
print(d[0:x])    


d = [0] * 30001
def top_down(x):
    if x == 1:
        return 0
    if d[x] != 0:
        return d[x]
    d[x] = top_down(x-1) + 1

    if(x%5 == 0):
        d[x] = min(d[x], top_down(x//5) + 1)

    if(x%3 == 0):
        d[x] = min(d[x], top_down(x//3) + 1)
    
    if(x%2 == 0):
        d[x] = min(d[x], top_down(x//2) + 1)
    
    return d[x]

print(top_down(x))
print(d[0:x])
    