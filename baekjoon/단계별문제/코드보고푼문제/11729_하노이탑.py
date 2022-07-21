count = 0

def hanoi_tower(n, start, end, li) :
    global count
    if n == 1 :
        li.append(f"{start} {end}")
        count += 1
        return
       
    hanoi_tower(n-1, start, 6-start-end, li) # 1단계
    li.append(f"{start} {end}") # 2단계
    count += 1
    hanoi_tower(n-1, 6-start-end, end, li) # 3단계
    return count
    
n = int(input())
ss = []
hanoi_tower(n, 1, 3, ss)
print(count)
print("\n".join(ss))