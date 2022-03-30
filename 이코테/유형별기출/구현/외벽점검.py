from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range (length):
        weak.append(weak[i] + n)
    
    result = int(1e9)
    for i in range(length):
        for j in permutations(dist, len(dist)):
            worker = 1
            position = weak[i] + j[worker-1]
            for index in weak[i:i+length]:
                if position < index:
                    worker += 1
                    if worker > len(dist):
                        break
                    position = index + j[worker-1]
            if worker < result:
                result = worker
    if result > len(dist):
        return -1
    return result