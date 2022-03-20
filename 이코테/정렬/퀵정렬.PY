## 1.
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    while left <= right: 
        # 2개 남은거 처음에 들어올 때 left == right
        # 한 번이라도 여기 돌면 left == right는 나올 수 없음
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)

## 2.
## 확실히 직관적이긴 함
## 비교 연산 횟수는 증가, 루프 반복수에 대해서는 동일
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_r(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x> pivot]

    return quick_sort_r(left_side) + [pivot] + quick_sort_r(right_side)

print(quick_sort_r(arr))