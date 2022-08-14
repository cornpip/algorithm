def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while arr[pivot] >= arr[left] and left< end:
            left += 1
        while arr[pivot] <= arr[right] and right > start:
            right -= 1
        if left >= right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)
    # return arr

arr = [15,15,15]
a = quick_sort(arr, 0, len(arr)-1) 
print(arr)           