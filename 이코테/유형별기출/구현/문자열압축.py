def solution(s):
    length = len(s)
    res = int(1e9)
    if length == 1:
        return 1
    for num in range (1, length):
        result = ""
        prev = ""
        count = 0
        for i in range(length//num):
            if i == 0:
                pre_index = 0
            now = s[pre_index: pre_index + num]
            pre_index = pre_index + num

            if i == (length//num - 1) :    
                if prev == "":
                    result += s[:]
    
                if prev == now:
                    count += 1
                    result += str(count)+prev
                
                if prev != now:
                    if count == 1:
                        result += prev + now
                    if count > 1:
                        result += str(count)+prev+now
                
                if length//num >= 1 and length % num > 0:
                    rest = length % num
                    result += s[-rest:]
                
                if res > len(result):
                    res = len(result)
                break

            if prev == "":
                count = 1
                prev = now
                continue

            if prev == now:
                count += 1
                prev = now
                continue
            if prev != now:
                if count == 1:
                    result += prev
                    prev = now
                    count = 1
                    continue
                if count > 1:
                    result += str(count)+prev
                    prev = now
                    count = 1
                    continue
    return  res