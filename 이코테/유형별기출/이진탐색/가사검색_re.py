from bisect import bisect_left, bisect_right

def count_range(a, left_val, right_val):
    left_index = bisect_left(a, left_val)
    right_index = bisect_right(a, right_val)
    return right_index - left_index

def solution(words, queries):
    result =[]
    word_list = [[] for _ in range(10001)]
    reverse_word = [[] for _ in range(10001)]
    for word in words:
        word_list[len(word)].append(word)
        reverse_word[len(word)].append(word[::-1])
    
    for i in range(1, 10001):
        word_list[i].sort()
        reverse_word[i].sort()

    for query in queries:
        if query[0] != "?":
            count = count_range(word_list[len(query)], query.replace("?","a"), query.replace("?","z"))
        else:
            count = count_range(reverse_word[len(query)], query[::-1].replace("?","a"), query[::-1].replace("?","z"))
        result.append(count)
    return result

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
a = solution(words, queries)
print(a)