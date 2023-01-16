#fc layer를 재귀로 만든다면?

## 할인율 알아서 적용하고 조건에 부합하는 최고의 결과를 return해라
## length에 따라 반복문의 depth를 정해야돼서 재귀 로 가져가야할 듯

def calcular(discounts: list, emoticons: list, users: list):
    # print("calcular")
    #각 이모티콘에 할인율은 recursion에서 fix
    subs = 0
    sales = 0
    # 한 유저에 대해 이모티콘s를 돌리자
    for discount_u, sale_u in users:
        buy_price = 0
        u_sub = False
        # 여기 루프는 한 사람당 모든 이모티콘
        for discount, emoticon in zip(discounts, emoticons):
            if discount_u > discount:
                pass #구매x
            else:
                buy_price += emoticon * (1 - (discount*0.01))
                if buy_price >= sale_u and not u_sub:
                    #구매x 이모티콘 플러스 가입
                    u_sub = True

        # 한 사람당 이모티콘의 연산이 끝나고
        if u_sub:
            subs += 1
        else:
            sales += buy_price
        # print(subs, sales, u_sub, buy_price, discounts)
    return [subs, sales] #subs_sales
                    
fix_percent = [10, 20, 30, 40]
# subs_sales return에 대한 판단은 recursion쪽에서
# 처음 discounts=[], depth=0
def recursion(emoticons: list, users: list, depth: int, length: int, discounts: list):
    # print("recursion", depth, discounts)
    subs_sales = [0, 0]
    if depth == length:
        try:
            subs, sales = calcular(discounts, emoticons, users) #완탐 안하려면 여기서 할인율보고 적당히 쳐내야하나?
            return [subs, sales]
        except Exception as e:
            print("here!!")
    
    else:
        try:
            for percent in fix_percent:
                discounts_c = [i for i in discounts[:]]
                discounts_c.append(percent) #append는 축약하지말고 그냥 순서하나 빼두자
                subs, sales = recursion(emoticons, users, depth+1, length, discounts_c)
                if subs > subs_sales[0]:
                    subs_sales = [subs, sales]
                elif subs == subs_sales[0]:
                    if sales > subs_sales[1]:
                        subs_sales = [subs, sales]
            return subs_sales
        except Exception as e:
            print(e)
            print("here!!2", subs_sales)
            

def solution(users, emoticons):
    return recursion(emoticons, users, 0, len(emoticons), [])