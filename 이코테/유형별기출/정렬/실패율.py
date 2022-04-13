def solution(n, stages):
    yap = [0 for _ in range(n+1)]
    for i in stages:
        yap[i-1] += 1
    
    fail = []
    length = len(stages)
    for i in range(len(yap)-1):
        if length == 0:
            a = 0
        else:
            a = yap[i]/length
        fail.append([i, a])
        length -= yap[i]
    
    fail.sort(key=lambda x: (-x[1], x[0]))
    result = []
    for i in fail:
        result.append(i[0]+1)
    return result


print(solution(3, [1, 1, 1]))