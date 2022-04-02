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
    u, v = yap(w)
    if check(u):
        # result += u
        recursive(v)
    else:
        recursive(u)

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
    result = ""
    hmm = check(fxxk)
    if hmm:
        return fxxk
    elif fxxk == "":
        return ""