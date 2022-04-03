def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
               return False
            count -= 1
    return True

def solution(p):
    result = ''
    if p == '':
        return result
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    if check_proper(u):
        result = u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        result += ''.join(u)
    return result 