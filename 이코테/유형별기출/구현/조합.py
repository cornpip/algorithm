def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combinations(arr[i+1:], r - 1):
                yield [arr[i]] + j

for combi in combinations([1,2,3,4,5],3):
    print(combi,end=" ")

# 조합 - 원소 내용으로 구분한건 아니다. / index기반으로 구분한 것
# [1,1,1,1,1] 5개중에 3개뽑는 수는 똑같다.
print()

# 위와 같은 역활의 함수를 제너레이터라 한다.
# generator : iterator를 생성해주는 함수

# yield가 함수를 iterable한 객체로 사용할 수 있게 해준다.
# ex)
def test(n):
    if n == 1:
        for i in range(5,9):
            yield i
        # yield 10
    else:
        for i in range(3):
            for j in test(1):
                yield (i, j)

for i in test(2):
    print(i)


# 이렇게 쓸 수도 있다.
print('-------------------')
a = test(2)
print(next(a))
print(next(a))
print(next(a))