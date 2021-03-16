lines = []
while True:
    a = input()
    line = list(map(int, a.split()))
    #split은 , 만들어주는거
    #map이 str >> int로
    if line and line !=[0,0,0]:
        lines.append(line)
    elif line == [0,0,0]:
        break
    else:
        break
num = len(lines)
for i in range(num):
    cross = max(lines[i])
    yap = lines[i].index(cross)
    del lines[i][yap]
    if lines[i][0]**2 + lines[i][1]**2 == cross**2:
        print('right')
    else :
        print('wrong')
    
