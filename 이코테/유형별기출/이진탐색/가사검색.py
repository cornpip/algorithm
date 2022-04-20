def remo(query):
    index = -1
    count = 0
    for i,val in enumerate(query):
        if val == "?":
            if index == -1:
                index = i
            count += 1
    if index == 0:
        return [index+count, True]
    else:
        return [True ,index]

def binary_remo(query):
    start, end = 0, len(query)-1
    left = True if query[0] == "?" else False
    final = True if query[-1] == "?" else False
    if left and final:
        return [False, False]
    while 1:
        mid = (start+end)//2
        if left:
            if query[mid] == "?":
                if query[mid+1] != "?":
                    return [mid+1, True]
                start = mid+1
            else:
                end = mid-1
        else:
            if query[mid] == "?": 
                if query[mid-1] != "?":
                    return [True, mid]
                end = mid-1
            else:
                start = mid+1
        

def solution(words, queries):
    result = []
    for query in queries:
        count = 0
        start, end = binary_remo(query)
        for word in words:
            if len(word) == len(query):
                if not start and not end:
                    count += 1
                elif type(start) == bool and start:
                    if word[:end] == query[:end]:
                        count += 1
                elif type(end) == bool and end:
                    if word[start:] == query[start:]:
                        count += 1
        result.append(count)
    return result

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
a = solution(words, queries)
print(a)