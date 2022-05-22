from itertools import combinations

vowel = {"a", "e", "i", "o", "u"} #영어는 모음 5개 끝

l, c = map(int, input().split())
password = input().split()
count1 = 0
count2 = 0
res = 0

for i in combinations( password, l ):
    for j in i:
        if j in vowel:
            count1 += 1
        else:
            count2 += 1
    if count1 > 0 and count2 >1:
        print("".join(i))
        res += 1
    count1, count2 = 0, 0

print(res)