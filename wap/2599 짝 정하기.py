n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

a,b,c,d,e,f = A[0],B[0],C[0],A[1],B[1],C[1]
valid = 1

for x in range(n+1):
    y = d-x-c+e
    z = x+c-e
    if( a-x >= 0 and y >= 0 and  b-y >= 0 and z >= 0 and c-z >= 0):
        print("1")
        print(x, a-x)
        print(y, b-y)
        print(z, c-z)
        valid = 0
        break
if valid :
    print('0')
    
