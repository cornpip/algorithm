from bisect import bisect_left

def F(m1, d, m2=1):
    return m1*m2/d**2 #python float 유효자리 15자리

def check(x, w, step, start, end):
    # print(step, start, end)
    l_idx = bisect_left(x, step)
    leftF, rightF = 0, 0
    for idx in range(len(x)):
        d = abs(x[idx] - step)
        # print(d)
        if idx < l_idx:
            leftF += F(w[idx], d)
        else:
            rightF += F(w[idx], d)

    # print(f"{leftF:.12f}, {rightF:.12f}")
    if leftF == rightF:
        return True, step, True, True

    # 여기부터 이진 탐색
    if leftF > rightF:
        n_step = (step+end)/2
        start = step
    else:
        n_step = (step+start)/2
        end = step

    if n_step in [start, end]:
        return True, step, True, True
    return False, n_step, start, end

# slicing은 깊은 복사, 2차원 리스트라면 안에까지 slicing하면 깊은 복사
for tc in range(int(input())):
    N = int(input())
    xw = list(map(int,input().split()))
    x = sorted(xw[:N])
    w = xw[N:]

    steps = []
    section = 0
    while 1:
        start, end = x[section], x[section + 1]
        step = (start + end) / 2
        while 1:
            ret, step, start, end = check(x, w, step, start, end)
            if ret:
                steps.append(f"{step:.10f}")
                break
        if section == len(x)-2:
            break
        section += 1

    steps = " ".join(steps)
    print(f"#{tc + 1} {steps}")
