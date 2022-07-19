# 1193
# 하나씩 접근하면 시간초과

x = int(input())

n = 1
while 1:
    hap = int(n*(n+1)/2)
    # print(n, hap)
    if x <= hap:
        if n % 2 == 0:
            now = [n, 1]
            while 1:
                if hap == x:
                    res = now
                    break
                now[0] -= 1
                now[1] += 1
                # 라인은 맞췄으니까 벗어나는 건 없겠지
                hap -= 1
        else:
            now = [1, n]
            while 1:
                if hap == x:
                    res = now
                    break
                now[0] += 1
                now[1] -= 1
                hap -= 1
        break
    n += 1

print(f"{res[0]}/{res[1]}")