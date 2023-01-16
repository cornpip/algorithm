from collections import deque

def solution(queue1, queue2):
    length = len(queue1)
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1s, q2s = sum(q1), sum(q2)
    
    count = 0
    while q1s != q2s:
        # 한건당 많이 써도 120만? 충분히 남아있어 근데 왜 걸리지?
        # sum이 O(n)이다. 반복안에 sum들어가 있으면 안됨
        if count > 3*length:
            count = -1
            break
            
        if q1s > q2s:
            tem = q1.popleft()
            q2.append(tem)
            q1s -= tem
            q2s += tem
        elif q1s < q2s:
            tem = q2.popleft()
            q1.append(tem)
            q2s -= tem
            q1s += tem
            
        count += 1
        
    return count