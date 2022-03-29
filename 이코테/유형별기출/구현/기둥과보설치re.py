def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:  
                # 한 좌표에 보하고 기둥을 동시에 세우는게 되나본데?
                # 구조물이 겹치도록 설치하는 경우가 없다 == 그냥 기둥기둥 이렇게 겹치는 것만 뜻한건가봐
                continue
            return False
        elif stuff == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, works):
    answer = []
    for work in works:
        x, y, stuff, operate = work
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)

# M (works) * M (answer loop) * MlogM(sort 정렬)
# answer loop와 sort정렬을 과하게 잡은거니까 대충 O(M^3)라 하는 듯 하다.
# 5초 짜리 문제라 1억 5천까지 고려해볼 수 있으므로
# M=1000이면 10억 인데?? 
# 실제 M^3보다 훨 작다 생각하고 해버리나...


# --- 
# 지우거나 설치할 때 특정케이스로 좁히는건 그럴 수 있는데
# (x, y)를 선택할 graph를 만들 이유가 없었다. 괜히 리스트만 복잡하게 됐지

# 들어오는 순서대로 할 건데 특정 좌표를 잡을 이유가 없다.
# 더욱이 return 하는건 들어온 좌표지 ( 임의로 정한 좌표가 아니라 )

# 총평 - 복잡하게 생각하지말고 return 해야할 것에 필요한가를 생각해보자.