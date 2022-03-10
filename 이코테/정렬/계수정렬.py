arr = [7, 2, 6, 0, 3, 1, 6, 2, 9, 1, 4, 8, 5, 0, 3, 2]

count = [0] * (max(arr) + 1)

for i, v in enumerate(arr):
    count[v] += 1

for i, v in enumerate(count):
    for j in range(v):
        # print 맘에 안들어서 추가
        if(i == len(count)-1 and j == v-1):
            print(i)
            break
        print(i, end=' ')

# 입력도 함수 돌면서 받는게 됐으니까
# 출력도 저렇게 나눠서 출력해도 되려나? ( 근데 저런식으로 출력을 요구하지 않을 듯 )

arr = [(2, 1), (3, 2), (1, 6)]

def flag(data):
    return data[0]

print(sorted(arr, key=flag))