from collections import deque
import copy

n = int(input())
k = int(input())
k_arr = []
for i in range(k):
    # k_arr 1행 1열 = [1,1]
    k_arr.append(list(map(int, input().split())))

l = int(input())
l_deq = deque()
for i in range(l):
    l_deq.append(input().split())



def snake():
    rotate = [["col", "+"], ["row", "+"], ["col", "-"], ["row", "-"]]
    now = deque()
    now.append([1,1])
    num = 0
    now_arrow = rotate[num]
    t = 0 
    while True:
        ## 머리 이동 (아 통째로 이동하면 안되지)
        t += 1
        # prev = copy.deepcopy(now[-1])
        if now_arrow[0] == "col":
            if now_arrow[1] == "+":
                new_now = [now[0][0], now[0][1] + 1]
                now.appendleft(new_now)
            else:
                new_now = [now[0][0], now[0][1] - 1]
                now.appendleft(new_now)
        else:
            if now_arrow[1] == "+":
                new_now = [now[0][0] + 1, now[0][1]]
                now.appendleft(new_now)
            else:
                new_now = [now[0][0] - 1, now[0][1]]
                now.appendleft(new_now)
        
        ## 벽 겹치는지 확인
        if now[0][0] > n or now[0][0] < 1 or now[0][1] > n or now[0][1] < 1:
            # print(now)
            # print('wall')
            return t
        
        ## 꼬리 생성 후 뱀 겹치는지 확인 // 문제가 좀 그렇네,꼬리도 머리랑 동시에가는게 맞지 ( 머리 먼저 꼬리나중에 따라오는 거네...)
        ## 그럼 꼬리 만들기 체크하지말고 먼저 머리 닿앗는지 보고 생성하란거네
        now_l = list(now)
        if now_l[0] in now_l[1:]:
            # print(now)
            # print('snake')
            return t
        
        ## 사과 체크 꼬리 생성
        if now[0] not in k_arr:
            # print('~~~~~~~~~~~~~~~~')
            now.pop()
            # print(now)
        else:
            k_arr.remove(now[0])
        
        ## 방향 t체크// 전환
        if l_deq:    
            if t == int(l_deq[0][0]):
                if l_deq[0][1] == "D":
                    num += 1
                    num %= 4
                    now_arrow = rotate[num]
                    l_deq.popleft()
                else:
                    num -= 1
                    num %= 4
                    now_arrow = rotate[num]
                    l_deq.popleft()

result = snake()
print(result)

## 예시case는 다 맞는데 머가 틀린거지

## 이럴 때 반례를 생각해보자

## 사과를 먹고 안지워서 그런가?

## 사과 다  먹고 index err나려나 

## 됐다...