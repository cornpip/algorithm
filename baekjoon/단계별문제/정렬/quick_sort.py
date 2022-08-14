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

# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))

arr = [ 2, 6, 7, 5, 9, 0, 1, 4, 3, 8]
quick_sort(arr, 0, len(arr)-1) 
# for i in arr:
#     print(i)
print(arr)

# 그냥 정렬 문제
# sort: 104ms, quick_sort: 160ms, 메모리는 비슷
# 백준 최대 재귀 깊이는 1,000 으로 제한되어 있다고함
# 재귀썼는데 RecursionError 나오면 고려