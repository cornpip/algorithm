case = int(input())
test = []

for i in range(case):
    a = input()
    line = list(map(int, a.split()))
    test.append(line)

for i in range(case):
    x = test[i][0]
    del test[i][0]
    y = sum(test[i])/x
    top = list(filter(lambda e: e>y, test[i]))
    top2 = len(top)
    position = top2/x * 100
    print('%.3f' %position + '%')    
    
