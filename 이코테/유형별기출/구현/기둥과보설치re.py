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