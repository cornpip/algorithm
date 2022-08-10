def z(m,r,c,count):
    left, up = True, True
    if r >= m/2:
        up = False
    if c >= m/2:
        left = False

    # if left and up: count그대로 

    if not left and up:
        c -= (m/2)
        count += (m/2)**2

    elif left and not up:
        r -= (m/2)
        count += (m/2)**2*2

    elif not left and not up:
        c -= (m/2)
        r -= (m/2)
        count += (m/2)**2*3

    if (m/2) == 1:
        return int(count)

    return z(m/2, r, c, count)

n, r, c = map(int, input().split())
print(z(2**n, r, c, 0))