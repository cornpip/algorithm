n, m = map(int, input().split())

data = []
for i in range(n):
    hi = list(map(int, input().split()))
    data.append(hi)

result = 0
for i in range(n):
    hello = data[i]
    minimum = min(hello)
    if(result):
        result = result if result>minimum else minimum
    elif( result == 0 ):
        result = minimum 

print(result)