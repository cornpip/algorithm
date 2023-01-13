import re

def compare(today: list, deadline: list):
    for t, d in zip(today, deadline):
        if d < t:
            # print(deadline, today)
            return True
        
        if d > t:
            return False
    return False

def deadline(info: list, terms_month: int):
    dead_year = int(info[0])
    dead_month = int(info[1]) + terms_month
    dead_day = int(info[2]) - 1
    
    if dead_month > 12: #12일때 안들어와 24고려
        mock = dead_month//12
        remain = dead_month%12
        if remain == 0:
            mock -= 1
            remain = 12
        
        dead_month = remain
        dead_year += mock
        
    if dead_day == 0:
        if dead_month == 1:
            dead_month = 12
            dead_year -= 1
        else:
            dead_month -= 1    
        dead_day = 28
    
    return [dead_year, dead_month, dead_day]

def solution(today, terms, privacies):
    terms_d = {}
    for term in terms:
        term_l = term.split(" ")
        terms_d[term_l[0]] = int(term_l[1])
    
    res = []
    for idx, privit in enumerate(privacies):
        privit_l = re.split('[.| ]', privit)
        
        deadline_l = deadline(privit_l[:3], terms_d[privit_l[3]])
        today_l = list(map(int, today.split(".")))
        
        if compare(today_l, deadline_l):
            res.append(idx+1)
    return res