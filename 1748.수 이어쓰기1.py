'''n = input()
m = int(n)
ret = 0
for i in range(1, m):
    ret += len(str(i))
print(ret)'''


'''n = int(input())
ret=0
for i in range(1, n+1):
    while i:
        i = i//10
        ret += 1
print(ret)'''

n= input()
n_len = len(n)-1
ret = 0
i = 0
while i< n_len:
    ret += 9*(10**i)*(i+1)
    i += 1
ret += ((int(n) - (10**n_len)) + 1) * (n_len+1)
print(ret)


