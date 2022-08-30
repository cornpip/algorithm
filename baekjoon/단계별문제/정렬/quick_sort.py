import sys
sys.setrecursionlimit(10000)

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while 1:
        while arr[pivot] >= arr[left] and left< end:
            left += 1
        while arr[pivot] <= arr[right] and right > start:
            right -= 1
        if left >= right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
            # print("break", arr)
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
        print(arr, left, right)
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

arr = [ 2, 6, 7, 5, 9, 0, 1, 4, 3, 8]
quick_sort(arr, 0, len(arr)-1) 
print(arr)

# 그냥 정렬 문제
# sort: 104ms, quick_sort: 160ms, 메모리는 비슷
# 백준 최대 재귀 깊이는 1,000 으로 제한되어 있다고함
# 재귀썼는데 RecursionError 나오면 고려

# +) quick_sort: arr잘라서 넘겨주고 return붙이는 식으로 가면 start, end 안가져갈 수도 있다.
# +) 아이디어 보다 구현에서 부등호가 헷갈린다