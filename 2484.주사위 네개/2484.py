a = int(input())
b = [list(map(int, input().split())) for _ in range(a)]
# for _ in 쓰려면 무조건 list 제일 겉에 둘러쌓야 하는듯


#input() for
#list(map(int, input().split()))

#b = [b.replace(" ",",")]
print(b)
print(b[1][2])

i=0
d=[]
for i in range(a):
    for j in range(1, 7):
        d.append(len(list(filter(lambda x : x==j ,b[i]))))

def divide(tlist, n):
    for i in range(0, len(tlist), n):
        yield tlist[i:i+n]
        
result = list(divide(d, 6))
print(result)
print(max(result[0]))

money = []
for i in range(a):
    sam = max(result[i])

    if sam == 4:
        money.append( 50000 + (result[i].index(4)+1)*5000 )
    elif sam == 3:
        money.append( 10000 + (result[i].index(3)+1)*1000 )
    elif sam == 2:
        c = list(filter(lambda x : result[i][x]==2 ,range(6)))
        if len(c) == 2:
            print(c[0]+1)
            print(c[1]+1)
            money.append( 2000 + (c[0]+1)*500 + (c[1]+1)*500 )
        else :
            money.append( 1000 + (c[0]+1)*100 )
    elif sam == 1:
        num1 = list(filter(lambda x : result[i][x]==True ,range(6)))
        num2 = max(num1)+1
        money.append( num2*100 )        

winmoney = max(money)
print(winmoney)

         
            
'''len(list(filter(lambda x : x==j ,b[i])))
c = filter(lambda x : x==1 ,b[0])
print(len(list(c)))'''

# filter가 아니라 index를 써야돼 index는 기본적으로 젤 첨 걸리고 끝내는데
# 여러개 뽑는 법 찾아보자


