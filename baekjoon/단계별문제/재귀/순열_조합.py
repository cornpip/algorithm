## retrun
def permutation(arr, res, n, check):
    if n == 0:
        print(res)
        return
    for i in range(len(arr)):
        if not check[i]:
            check[i] = True
            res.append(arr[i])
            permutation(arr, res, n-1, check)
            res.pop(-1)
            check[i] = False

def combination(arr, res, n, idx):
    if n == 0:
        print(res)
        return
    for i in range(idx, len(arr)):
        res.append(arr[i])
        combination(arr, res, n-1, i+1)
        res.pop(-1)

arr = [1,2,3,4]
res = []
check = [ False for _ in range(len(arr)) ]
# permutation(arr, res, 2, check)
# combination(arr, res, 2, 0)

def gen_combinations(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            result.append([elem]+C) 
              
    return result
# print(gen_combinations(arr, 2))

## generator
def permutation_g(arr, n, now=-1):
    for i in range(len(arr)):
        if i == now:
            continue
        if n == 1:
            yield [arr[i]]
        else:
            for j in permutation_g(arr, n-1, i):
                yield [arr[i]] + j

def combination_g(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for j in combination_g(arr[i+1:], n-1):
                yield [arr[i]] + j

# for i in combination_g(arr, 2):
#     print(i)

# for i in permutation_g(arr, 2):
#     print(i)