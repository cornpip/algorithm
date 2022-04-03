def yap(w):
    prev = ""
    u, v = "", ""
    count, turn = 0, False
    for i, sxxk in enumerate(w):
        if turn:
            if prev==sxxk:
                count -= 1
                if count == 0:
                    u += w[:i+1]
                    v += w[i+1:]
                    return u, v
                prev = sxxk
            else:
                turn = False
                count += 1
                prev = sxxk

        else:
            if prev=="" or prev==sxxk:
                count += 1
                prev = sxxk
            else:
                count -= 1
                if count == 0:
                    u += w[:i+1]
                    v += w[i+1:]
                    return u, v
                prev = sxxk
                turn = True

def recursive(w):
    if w == "":
        return ""
    result = ""
    hap = yap(w)
    u, v = hap[0], hap[1]
    if check(u):
        result += u + recursive(v)
    else:
        result = "("
        result += recursive(v)
        result += ")"
        u = list(u[1:-1])
        for i,val in enumerate (u):
            if val == "(":
                u[i] = ")"
            else:
                u[i] = "("
        for i in u:
            result += i
    return result

def check(w):
    count = 0
    for i in w:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(fxxk):
    hmm = check(fxxk)
    if hmm:
        return fxxk
    elif fxxk == "":
        return ""
    return recursive(fxxk)

a = "))()(("
print(solution(a))